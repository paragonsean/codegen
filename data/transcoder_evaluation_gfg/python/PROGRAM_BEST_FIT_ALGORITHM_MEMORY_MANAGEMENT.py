# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( blockSize , m , processSize , n ) :
    allocation = [ - 1 ] * n
    for i in range ( n ) :
        bestIdx = - 1
        for j in range ( m ) :
            if blockSize [ j ] >= processSize [ i ] :
                if bestIdx == - 1 :
                    bestIdx = j
                elif blockSize [ bestIdx ] > blockSize [ j ] :
                    bestIdx = j
        if bestIdx != - 1 :
            allocation [ i ] = bestIdx
            blockSize [ bestIdx ] -= processSize [ i ]
    print ( "Process No.Process Size     Block no." )
    for i in range ( n ) :
        print ( i + 1 , "         " , processSize [ i ] , end = "         " )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        else :
            print ( "Not Allocated" )


#TOFILL

if __name__ == '__main__':
    param = [
    ([1, 12, 63, 99, 99],2,[8, 11, 35, 64, 93],3,),
    ([-72, -60, 22, 88, 90, -36, 98, -42, 72, 16, -36, 30, -24, -2, 92, 50, -96, -12, -42, 14, -62, 70, -84, -30, -20, 4, -36, -8, 16, 88, 58, -92, -84, 40, -12, 50],24,[-98, 96, -92, -98, -48, -64, 16, -94, -30, 58, 0, 14, -30, -30, 70, -72, 8, -8, 84, -24, -74, 2, -24, 20, 12, 46, 30, 2, -2, -74, 82, -96, 44, -68, -58, -52],23,),
    ([0, 1],1,[0, 1],1,),
    ([50, 45, 11, 24, 93, 76, 89, 90, 63, 40, 84, 47, 9, 90, 61, 11, 46, 63, 16, 80, 99, 65],21,[64, 56, 53, 46, 97, 91, 50, 68, 32, 83, 69, 57, 59, 99, 61, 6, 90, 61, 9, 47, 93, 86],12,),
    ([-64, -26, 76],1,[-88, 44, 58],2,),
    ([0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1],40,[1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],36,),
    ([1, 2, 3, 3, 8, 9, 10, 10, 11, 18, 18, 19, 22, 23, 24, 27, 27, 27, 33, 36, 38, 39, 40, 41, 48, 50, 50, 51, 59, 59, 62, 65, 68, 69, 70, 71, 72, 72, 75, 75, 76, 84, 85, 86, 88, 91, 96, 99],36,[6, 14, 14, 21, 24, 25, 27, 29, 29, 30, 33, 38, 39, 44, 49, 50, 50, 51, 52, 52, 53, 54, 56, 56, 59, 59, 63, 64, 67, 68, 70, 71, 71, 72, 73, 73, 78, 80, 83, 84, 85, 87, 90, 91, 91, 92, 94, 96],43,),
    ([-58, -62, 82, -88],3,[38, 92, 76, 6],3,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],16,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],18,),
    ([13, 37, 2, 83, 4, 55, 76, 94, 74, 33, 99, 9, 62, 32, 45, 31, 40, 67, 47, 29, 70, 42, 93, 66, 78, 57, 27, 50, 17, 32, 18, 96, 52, 50, 99, 60, 4, 68, 34, 24, 26, 41, 23, 72, 93, 93, 39, 3],43,[53, 65, 91, 70, 65, 77, 70, 52, 89, 39, 22, 76, 95, 98, 85, 11, 27, 43, 39, 56, 44, 53, 63, 86, 32, 71, 5, 71, 85, 80, 41, 27, 52, 66, 4, 64, 99, 99, 92, 82, 17, 48, 41, 18, 79, 22, 62, 40],37,)
        ]
    filled_function_param = [
    ([1, 12, 63, 99, 99],2,[8, 11, 35, 64, 93],3,),
    ([-72, -60, 22, 88, 90, -36, 98, -42, 72, 16, -36, 30, -24, -2, 92, 50, -96, -12, -42, 14, -62, 70, -84, -30, -20, 4, -36, -8, 16, 88, 58, -92, -84, 40, -12, 50],24,[-98, 96, -92, -98, -48, -64, 16, -94, -30, 58, 0, 14, -30, -30, 70, -72, 8, -8, 84, -24, -74, 2, -24, 20, 12, 46, 30, 2, -2, -74, 82, -96, 44, -68, -58, -52],23,),
    ([0, 1],1,[0, 1],1,),
    ([50, 45, 11, 24, 93, 76, 89, 90, 63, 40, 84, 47, 9, 90, 61, 11, 46, 63, 16, 80, 99, 65],21,[64, 56, 53, 46, 97, 91, 50, 68, 32, 83, 69, 57, 59, 99, 61, 6, 90, 61, 9, 47, 93, 86],12,),
    ([-64, -26, 76],1,[-88, 44, 58],2,),
    ([0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1],40,[1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],36,),
    ([1, 2, 3, 3, 8, 9, 10, 10, 11, 18, 18, 19, 22, 23, 24, 27, 27, 27, 33, 36, 38, 39, 40, 41, 48, 50, 50, 51, 59, 59, 62, 65, 68, 69, 70, 71, 72, 72, 75, 75, 76, 84, 85, 86, 88, 91, 96, 99],36,[6, 14, 14, 21, 24, 25, 27, 29, 29, 30, 33, 38, 39, 44, 49, 50, 50, 51, 52, 52, 53, 54, 56, 56, 59, 59, 63, 64, 67, 68, 70, 71, 71, 72, 73, 73, 78, 80, 83, 84, 85, 87, 90, 91, 91, 92, 94, 96],43,),
    ([-58, -62, 82, -88],3,[38, 92, 76, 6],3,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],16,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],18,),
    ([13, 37, 2, 83, 4, 55, 76, 94, 74, 33, 99, 9, 62, 32, 45, 31, 40, 67, 47, 29, 70, 42, 93, 66, 78, 57, 27, 50, 17, 32, 18, 96, 52, 50, 99, 60, 4, 68, 34, 24, 26, 41, 23, 72, 93, 93, 39, 3],43,[53, 65, 91, 70, 65, 77, 70, 52, 89, 39, 22, 76, 95, 98, 85, 11, 27, 43, 39, 56, 44, 53, 63, 86, 32, 71, 5, 71, 85, 80, 41, 27, 52, 66, 4, 64, 99, 99, 92, 82, 17, 48, 41, 18, 79, 22, 62, 40],37,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))