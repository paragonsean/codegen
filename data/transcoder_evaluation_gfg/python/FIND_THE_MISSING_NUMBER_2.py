# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( a , n ) :
    x1 = a [ 0 ]
    x2 = 1
    for i in range ( 1 , n ) :
        x1 = x1 ^ a [ i ]
    for i in range ( 2 , n + 2 ) :
        x2 = x2 ^ i
    return x1 ^ x2


#TOFILL

if __name__ == '__main__':
    param = [
    ([2, 5, 7, 8, 10, 14, 27, 32, 51, 52, 57, 58, 65, 68, 68, 72, 73, 73, 83, 92, 98],12,),
    ([-60, -48, 38, -78, 88, 86, -4, -94, 16, -64, 32, 88, 58, -78, -16, 48, 38, 30, 66, -60, 20, 40, -28, -64, -48, -86, -80, -8, -58, 52, 80, -32, 46, -4, -70, 76, -4, 78, -64, 38, -40],28,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],38,),
    ([69, 59, 22, 33, 69, 28, 11, 34, 72, 88, 16, 30, 69, 89, 43, 4, 65, 85, 27],13,),
    ([-98, -98, -92, -88, -88, -82, -74, -70, -68, -60, -60, -48, -38, -34, -34, -24, 14, 38, 50, 58, 62, 64, 64, 68, 76, 78, 78, 86, 88, 90, 92, 98, 98],23,),
    ([0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],41,),
    ([1, 9, 12, 12, 24, 25, 33, 33, 36, 39, 46, 48, 48, 52, 52, 53, 57, 69, 71, 72, 75, 76, 78, 80, 82, 86, 89, 91, 94, 95, 96, 97, 98, 99],30,),
    ([62, -66, 60, -92, 46, 6, -52, 48, 72, -64, 34, 20, 50, 70, -34, 20, -70, 14, -44, 66, -70],17,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],30,),
    ([33, 10, 6, 71, 18, 22, 15, 57, 56, 63, 35, 93, 31, 43, 98, 99, 62, 39, 44, 86, 78, 95, 6, 76, 71],12,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))