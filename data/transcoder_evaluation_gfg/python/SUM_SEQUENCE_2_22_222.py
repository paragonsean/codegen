# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import math

def f_gold ( n ) :
    return 0.0246 * ( math.pow ( 10 , n ) - 1 - ( 9 * n ) )


#TOFILL

if __name__ == '__main__':
    param = [
    (88,),
    (79,),
    (7,),
    (36,),
    (23,),
    (10,),
    (27,),
    (30,),
    (71,),
    (6,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if abs(1 - (0.0000001 + abs(f_gold(*parameters_set))) / (abs(f_filled(*parameters_set)) + 0.0000001)) < 0.001:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))