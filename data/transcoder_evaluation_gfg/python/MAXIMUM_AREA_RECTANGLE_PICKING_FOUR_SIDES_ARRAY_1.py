# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n ) :
    s = [ ]
    first = 0
    second = 0
    for i in range ( n ) :
        if arr [ i ] not in s :
            s.append ( arr [ i ] )
            continue
        if ( arr [ i ] > first ) :
            second = first
            first = arr [ i ]
        elif ( arr [ i ] > second ) :
            second = arr [ i ]
    return ( first * second )


#TOFILL

if __name__ == '__main__':
    param = [
    ([4, 6, 7, 8, 12, 13, 14, 15, 18, 18, 19, 19, 26, 26, 32, 32, 33, 34, 34, 36, 41, 43, 47, 47, 51, 51, 52, 53, 55, 56, 57, 60, 61, 71, 74, 75, 76, 77, 79, 87, 87, 87, 90, 95, 98, 99],37,),
    ([-64, -72, 6, -62, 54, 14, 28, 60, -96, 14, -32, -2, 80, 8, -56, 68, 86, 64, 86, -12, 82],12,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],27,),
    ([99, 7, 14, 50, 94, 24, 79, 13, 19, 29, 22, 2, 77, 36, 38, 18, 51, 15, 99, 52, 17, 77, 22, 54],15,),
    ([-96, -92, -86, -84, -84, -80, -70, -70, -68, -64, -64, -48, -46, -24, -22, -20, -8, -8, 0, 0, 4, 8, 8, 22, 28, 36, 46, 50, 52, 54, 60, 62, 66, 70, 80, 84, 86, 94, 96, 96],25,),
    ([1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],12,),
    ([98],0,),
    ([-88, -24, 8, 20, -46, 60, 24, 26, 98, 82, -30, 16, 22, -28, 84, 12, 34, 14, -18, -38, -94, -24, 6, 4, -52, -48, 84],21,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],21,),
    ([6, 30, 47, 97, 20, 16, 68, 34, 1, 77, 48, 8, 22, 68],8,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))