# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( a , n ) :
    count = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if ( a [ i ] & a [ j ] ) == 0 :
                count += 2
    return count


#TOFILL

if __name__ == '__main__':
    param = [
    ([17, 20, 32, 35, 35, 36, 43, 47, 59, 59, 68, 69, 70, 70, 75, 82, 88, 94, 96, 99],17,),
    ([-78, -40, 58, -36, 34, -12, -38, 48, -66, 16, 50, -26, -22, 46, -70, -68, -44, -52, -78, -50],11,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],23,),
    ([49, 57, 17, 37, 56, 61, 10, 3, 33, 33, 70, 35, 50, 85, 48, 65, 83, 21, 96, 19, 66, 43, 69, 17, 60, 87, 82, 3, 83, 44, 63, 19, 55, 58, 77, 76, 50, 96],37,),
    ([-94, -88, -86, -80, -80, -72, -64, -60, -58, -58, -58, -50, -44, -32, -8, -8, 0, 6, 8, 10, 14, 14, 18, 28, 34, 34, 46, 54, 56, 56, 56, 64, 66, 66, 70, 82, 84, 88, 96],33,),
    ([1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],13,),
    ([1, 3, 10, 11, 13, 14, 15, 17, 20, 25, 26, 26, 27, 29, 32, 36, 36, 36, 42, 46, 47, 49, 51, 54, 54, 55, 60, 66, 67, 68, 68, 68, 72, 77, 78, 79, 83, 84, 92, 98],32,),
    ([-76, -72, 16, 38, -60, 44, -2, -76, -76, -56, 40, 36, 50, -50, -32, 48, -96, 80, 84, 60, 84, 38, -54, -42, 48, 30, 66, -62, -52, -94, 64, -16, 54, 98],28,),
    ([0, 0, 1, 1, 1, 1],5,),
    ([63, 82, 22, 84, 11, 62, 18, 43, 57, 25, 4, 27, 62, 46, 55, 16, 1, 9, 10, 73, 36, 80, 95, 87, 47, 64, 27, 25, 70],22,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))