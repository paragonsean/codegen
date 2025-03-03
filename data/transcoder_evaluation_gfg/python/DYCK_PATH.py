# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    res = 1
    for i in range ( 0 , n ) :
        res *= ( 2 * n - i )
        res /= ( i + 1 )
    return res / ( n + 1 )


#TOFILL

if __name__ == '__main__':
    param = [
    (72,),
    (90,),
    (61,),
    (28,),
    (70,),
    (13,),
    (7,),
    (98,),
    (99,),
    (67,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))