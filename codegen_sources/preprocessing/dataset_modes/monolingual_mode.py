# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import sys
from logging import getLogger
from pathlib import Path

import submitit
import typing as tp
from codegen_sources.preprocessing.dataset_modes.dataset_mode import DatasetMode
from codegen_sources.preprocessing.lang_processors import LangProcessor
from codegen_sources.preprocessing.obfuscation.utils_deobfuscation import REPLACE_DICT
from codegen_sources.preprocessing import bpe_modes
from codegen_sources.preprocessing.timeout import timeout
from codegen_sources.preprocessing.utils import get_subset_file, is_valid_file

MONOLINGUAL_SUFFIXES = ["monolingual"]
logger = getLogger()


class MonolingualMode(DatasetMode):
    """
    Callable where we track the repos processed so that we can checkpoint with submitit
    """

    def __init__(
        self,
        folder,
        languages,
        bpe,
        processed_lines: tp.Optional[tp.Set] = None,
        nb_train_split: int = 8,
        keep_comments: bool = False,
        repo_split: bool = True,
    ):
        super().__init__(
            suffixes=MONOLINGUAL_SUFFIXES,
            folder=folder,
            languages=languages,
            bpe=bpe,
            parallel_dataset=False,
            processed_lines=processed_lines,
            nb_train_split=nb_train_split,
            keep_comments=keep_comments,
            repo_split=repo_split,
        )

    # broken as non-callable
    # def checkpoint(
    #     self, input_path: str, process_strings: bool
    # ) -> submitit.helpers.DelayedSubmission:
    #     return submitit.helpers.DelayedSubmission(
    #         self.__class__(
    #             self.folder, self.languages, self.bpe, self.processed_lines,
    #         ),
    #         input_path,
    #         process_strings,
    #     )

    def extract_data_for_line(
        self,
        line_id: str,
        json_line: dict,
        process_strings: bool,
        lang_processor: LangProcessor,
    ):
        default_return = line_id, None, None

        if "content" not in json_line:
            return default_return
        content = json_line["content"]
        for k, v in REPLACE_DICT.items():
            content = content.replace(k, v)
        tokenize = lang_processor.tokenize_code
        try:
            return (
                line_id,
                json_line["repo_name"],
                {
                    "monolingual": [
                        " ".join(
                            tokenize(
                                content,
                                process_strings=process_strings,
                                keep_comments=self.keep_comments,
                            )
                        )
                    ]
                },
            )
        except KeyboardInterrupt:
            raise
        except Exception as e:
            sys.stderr.write(f"Error tokenizing content {e}")
            return default_return

    def _learn_bpe(
        self, ncodes: int, executor: tp.Optional["ExecutorLike"] = None
    ) -> None:
        # get data to training data for bpe
        assert (
            len(self.suffixes) == 1
        ), "too many suffixes for dataset, cannot compute BPE safely."
        all_shufs = [
            self.folder.joinpath(f"{lang}.all.{self.suffixes[0]}.tok.shuf")
            for lang in self.languages
        ]
        if any(not shuf.is_file() for shuf in all_shufs):
            self.regroup_all_tok()
            self.shuffle_all_tok()
        assert all(shuf.is_file() for shuf in all_shufs)
        data_train_bpe = get_subset_file(
            file_paths=all_shufs,
            subset_size_gb=50,
            output_path=self.folder.joinpath(
                f"{'-'.join(self.languages)}.{self.suffixes[0]}.tok.shuf.{50}gb"
            ),
        )

        # train bpe codes
        assert isinstance(self.bpe, bpe_modes.FastBPEMode)
        logger.info(f"training bpe on {data_train_bpe}...")
        if executor is None:
            executor = submitit.LocalExecutor(self.folder.joinpath("log"))
        job = executor.submit(self.bpe.learn_bpe_file, data_train_bpe, ncodes)
        job.result()
        assert is_valid_file(
            self.bpe.codes
        ), f"Invalid filepath {self.bpe.codes} for {self.bpe}"
        logger.info(f"Successfully learnt bpe. Bpe codes stored in {self.bpe.codes}.")

    def _get_vocab(self, executor: tp.Optional["ExecutorLike"] = None) -> None:
        # get data to learn vocab
        assert isinstance(self.bpe, bpe_modes.FastBPEMode)
        data_get_vocab_list = [
            self.folder.joinpath(f"{lang}.train.{self.suffixes[0]}.0.bpe")
            for lang in self.languages
        ]
        data_get_vocab = get_subset_file(
            data_get_vocab_list,
            20,
            output_path=self.folder.joinpath(
                f"{'-'.join(self.languages)}.train.{self.suffixes[0]}.0.20BG.bpe"
            ),
        )
        assert Path(
            data_get_vocab
        ).is_file(), f"cannot get vocab, {data_get_vocab} doesnt not exist."

        # get vocab
        logger.info(f"Getting vocab from {data_get_vocab} ...")
        if executor is None:
            executor = submitit.LocalExecutor(folder=self.folder.joinpath("log"))
        job = executor.submit(self.bpe.get_vocab_file, data_get_vocab)
        job.result()
        assert self.bpe.vocab_path is not None and self.bpe.vocab_path.is_file()
        logger.info(f"Successfully got vocab. Vocab stored in {self.bpe.vocab_path}.")
