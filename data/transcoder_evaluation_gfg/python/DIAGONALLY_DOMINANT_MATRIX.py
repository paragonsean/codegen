# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( m , n ) :
    for i in range ( 0 , n ) :
        sum = 0
        for j in range ( 0 , n ) :
            sum = sum + abs ( m [ i ] [ j ] )
        sum = sum - abs ( m [ i ] [ i ] )
        if ( abs ( m [ i ] [ i ] ) < sum ) :
            return False
    return True


#TOFILL

if __name__ == '__main__':
    param = [
    ([[ 3, -2, 1 ], [ 1, -3, 2 ], [ -1, 2, 4 ]],2,),
    ([[ 2, -2, 1 ], [ 1, -3, 2 ], [ -1, 2, 4 ]],3,),
    ([[78, 46, 33, 58, 79, 94, 94, 31, 69], [83, 48, 11, 74, 33, 61, 88, 15, 29], [27, 20, 36, 14, 37, 88, 49, 36, 58], [93, 15, 39, 5, 97, 45, 1, 47, 34], [8, 88, 54, 87, 60, 77, 37, 46, 18], [10, 68, 71, 86, 76, 24, 47, 37, 72], [84, 43, 82, 25, 87, 18, 51, 46, 75], [59, 39, 78, 86, 38, 55, 79, 5, 5], [50, 42, 19, 34, 53, 80, 21, 45, 96]],1,),
    ([[88, 35, 82, 14, 86, 94, 12, 49, 76, 94, 3, 96, 27, 92, 82, 25, 15, 27, 15], [30, 75, 59, 45, 53, 78, 45, 92, 72, 61, 11, 78, 51, 86, 89, 74, 39, 24, 6], [33, 22, 60, 20, 11, 35, 35, 65, 90, 78, 49, 66, 46, 5, 39, 79, 85, 93, 51], [21, 38, 36, 14, 33, 23, 72, 84, 38, 47, 64, 47, 1, 42, 68, 78, 86, 76, 25], [57, 52, 7, 7, 56, 39, 70, 83, 58, 23, 10, 72, 36, 71, 3, 72, 77, 95, 13], [90, 48, 66, 3, 63, 15, 2, 61, 59, 17, 11, 5, 70, 67, 23, 96, 63, 4, 29], [17, 95, 35, 48, 85, 87, 48, 95, 53, 65, 75, 1, 7, 77, 84, 70, 30, 70, 98], [99, 84, 38, 30, 97, 54, 88, 95, 16, 16, 27, 22, 15, 46, 1, 28, 33, 15, 95], [57, 70, 68, 58, 20, 4, 10, 7, 91, 57, 6, 55, 31, 64, 36, 91, 13, 75, 73], [72, 61, 10, 66, 24, 99, 34, 50, 75, 1, 5, 27, 7, 1, 32, 17, 18, 68, 49], [13, 69, 22, 26, 68, 87, 5, 9, 77, 62, 73, 68, 90, 78, 2, 95, 50, 51, 90], [2, 41, 64, 44, 52, 37, 66, 92, 56, 23, 71, 39, 86, 60, 56, 36, 1, 98, 4], [41, 99, 53, 31, 33, 5, 43, 11, 32, 1, 43, 6, 92, 81, 11, 41, 27, 61, 76], [13, 95, 35, 25, 94, 36, 21, 55, 36, 28, 27, 12, 74, 26, 93, 45, 6, 89, 8], [75, 17, 38, 77, 41, 15, 83, 83, 74, 28, 25, 79, 35, 80, 37, 27, 5, 59, 88], [66, 99, 57, 61, 97, 96, 60, 64, 32, 16, 44, 87, 90, 69, 61, 71, 34, 74, 86], [21, 19, 52, 42, 39, 45, 89, 13, 43, 83, 71, 95, 66, 45, 4, 1, 60, 50, 87], [47, 17, 86, 35, 8, 56, 60, 55, 7, 65, 25, 24, 97, 75, 96, 93, 65, 47, 8], [45, 29, 31, 57, 99, 7, 31, 60, 56, 32, 94, 61, 61, 76, 99, 64, 10, 26, 69]],2,),
    ([[97, 37, 30, 97, 2, 42, 68, 90, 94], [35, 10, 31, 79, 85, 6, 65, 74, 2], [9, 81, 80, 66, 80, 99, 59, 92, 13], [6, 25, 63, 59, 90, 46, 15, 66, 86], [42, 92, 17, 23, 15, 38, 56, 34, 94], [65, 80, 89, 87, 97, 34, 73, 16, 50], [69, 42, 62, 12, 69, 87, 72, 99, 80], [84, 28, 30, 75, 50, 17, 10, 88, 95], [11, 47, 8, 31, 37, 33, 9, 46, 3]],4,),
    ([[28, 52, 61, 24, 10, 42, 37, 15, 28, 37, 65, 13, 59], [68, 56, 30, 64, 67, 20, 99, 27, 12, 41, 80, 96, 51], [97, 80, 29, 91, 95, 51, 59, 88, 31, 9, 70, 30, 90], [40, 7, 72, 59, 11, 3, 4, 97, 20, 5, 34, 14, 13], [61, 49, 45, 53, 24, 94, 63, 75, 9, 63, 56, 77, 77], [96, 71, 75, 42, 1, 64, 92, 72, 15, 69, 22, 20, 68], [45, 89, 80, 40, 46, 91, 63, 93, 12, 52, 7, 88, 55], [5, 47, 97, 38, 43, 70, 8, 86, 50, 78, 9, 13, 50], [96, 78, 35, 25, 61, 31, 49, 43, 45, 84, 7, 74, 6], [89, 50, 70, 45, 54, 17, 86, 87, 29, 64, 71, 99, 20], [26, 93, 29, 7, 34, 5, 77, 6, 96, 33, 43, 59, 33], [83, 61, 18, 14, 21, 39, 34, 31, 81, 7, 85, 71, 1], [86, 22, 87, 92, 63, 62, 46, 57, 94, 45, 74, 76, 80]],10,),
    ([[68, 37, 94, 90, 14, 37, 89, 91, 14, 66, 66, 33, 2], [98, 53, 89, 55, 45, 37, 27, 90, 52, 86, 47, 58, 7], [13, 48, 28, 45, 56, 92, 88, 35, 55, 97, 37, 9, 3], [2, 58, 22, 85, 24, 78, 54, 97, 17, 58, 58, 21, 77], [63, 63, 44, 40, 75, 66, 92, 67, 79, 46, 24, 72, 70], [96, 51, 99, 77, 92, 4, 31, 65, 30, 72, 40, 14, 44], [92, 34, 39, 4, 88, 27, 42, 11, 87, 32, 50, 53, 4], [19, 71, 33, 78, 77, 70, 83, 55, 9, 62, 99, 62, 48], [90, 68, 48, 92, 27, 55, 44, 71, 52, 57, 9, 98, 8], [56, 10, 65, 72, 45, 39, 46, 17, 82, 98, 99, 67, 76], [62, 68, 36, 9, 35, 67, 89, 52, 90, 91, 28, 58, 83], [24, 59, 37, 38, 25, 98, 15, 16, 55, 4, 26, 39, 57], [47, 90, 48, 92, 49, 37, 38, 62, 61, 74, 97, 8, 38]],7,),
    ([[85, 56, 45, 50, 20, 63, 55, 34, 92, 32, 76, 73, 43, 79, 13, 2, 61, 84, 14, 42, 15, 93, 85, 10, 56, 53, 58, 85, 99, 81, 62, 57, 63, 4, 78, 96], [82, 34, 32, 78, 34, 70, 40, 35, 15, 51, 20, 92, 37, 38, 21, 88, 10, 54, 9, 86, 42, 16, 24, 4, 44, 23, 42, 86, 66, 92, 19, 20, 28, 24, 91, 2], [7, 1, 11, 51, 60, 31, 30, 77, 24, 18, 58, 77, 17, 46, 94, 19, 12, 90, 82, 12, 50, 66, 20, 6, 1, 90, 7, 96, 55, 97, 74, 15, 95, 24, 29, 82], [71, 34, 78, 84, 93, 37, 42, 64, 95, 19, 23, 71, 6, 99, 93, 55, 77, 39, 25, 98, 83, 4, 88, 33, 66, 2, 14, 50, 11, 34, 38, 92, 39, 22, 42, 97], [95, 57, 78, 38, 9, 88, 29, 69, 42, 60, 39, 91, 72, 93, 60, 53, 76, 8, 21, 56, 48, 47, 9, 78, 1, 55, 31, 80, 91, 11, 66, 60, 31, 50, 60, 88], [62, 39, 3, 58, 68, 30, 67, 68, 58, 77, 53, 14, 10, 78, 81, 22, 63, 61, 46, 37, 21, 89, 3, 19, 32, 79, 24, 73, 74, 48, 96, 58, 40, 7, 46, 91], [15, 85, 74, 87, 5, 59, 70, 22, 28, 54, 19, 14, 48, 7, 79, 32, 22, 46, 85, 83, 13, 22, 10, 44, 24, 59, 62, 72, 72, 55, 49, 50, 19, 82, 58, 97], [48, 93, 96, 72, 96, 12, 86, 20, 45, 26, 81, 98, 31, 82, 59, 3, 18, 84, 21, 57, 99, 42, 62, 30, 61, 36, 55, 4, 15, 71, 96, 97, 57, 63, 77, 64], [17, 53, 40, 70, 50, 68, 15, 72, 34, 30, 87, 73, 24, 8, 57, 70, 25, 77, 34, 25, 18, 73, 97, 70, 14, 6, 82, 90, 36, 36, 75, 18, 15, 94, 89, 16], [76, 14, 47, 54, 58, 77, 30, 46, 16, 1, 41, 93, 27, 77, 62, 81, 28, 20, 55, 51, 69, 88, 73, 97, 34, 27, 97, 38, 29, 35, 20, 19, 5, 25, 93, 26], [51, 66, 61, 15, 45, 6, 58, 1, 73, 43, 16, 14, 74, 19, 51, 8, 48, 12, 70, 35, 70, 6, 99, 11, 38, 91, 26, 28, 72, 89, 83, 80, 50, 58, 26, 44], [15, 76, 24, 77, 59, 57, 17, 77, 81, 1, 11, 20, 31, 99, 39, 63, 6, 99, 28, 51, 53, 44, 65, 80, 12, 28, 79, 72, 68, 95, 30, 35, 6, 85, 30, 80], [63, 8, 91, 33, 43, 76, 43, 45, 87, 54, 65, 7, 36, 25, 85, 37, 12, 32, 49, 38, 56, 80, 65, 26, 57, 14, 56, 70, 41, 51, 84, 67, 12, 97, 49, 1], [19, 66, 58, 87, 72, 98, 4, 8, 27, 26, 97, 43, 40, 50, 67, 73, 74, 29, 85, 42, 18, 81, 21, 67, 62, 27, 96, 93, 47, 93, 26, 9, 91, 12, 16, 47], [56, 66, 51, 27, 73, 66, 62, 71, 8, 38, 6, 59, 19, 79, 56, 28, 94, 91, 10, 45, 95, 65, 50, 32, 61, 16, 6, 66, 62, 66, 67, 19, 4, 43, 18, 82], [46, 46, 85, 21, 30, 64, 41, 17, 5, 5, 73, 75, 48, 78, 38, 6, 58, 14, 72, 94, 59, 65, 89, 13, 27, 25, 56, 68, 59, 95, 49, 18, 81, 75, 76, 3], [79, 57, 6, 69, 31, 8, 10, 3, 12, 92, 76, 94, 19, 21, 81, 14, 75, 29, 7, 49, 65, 7, 14, 16, 99, 16, 85, 13, 82, 29, 85, 73, 95, 61, 37, 17], [31, 59, 88, 47, 6, 32, 31, 18, 9, 3, 71, 26, 13, 34, 43, 93, 33, 69, 36, 79, 74, 68, 47, 61, 45, 96, 88, 84, 48, 41, 38, 68, 75, 11, 16, 65], [97, 71, 67, 71, 1, 97, 71, 4, 82, 37, 14, 79, 25, 82, 4, 66, 43, 26, 84, 15, 6, 37, 43, 42, 13, 16, 42, 38, 66, 65, 5, 30, 95, 43, 32, 67], [67, 42, 5, 99, 86, 96, 59, 23, 8, 68, 70, 91, 19, 44, 93, 38, 44, 6, 3, 96, 80, 33, 66, 58, 26, 99, 28, 43, 75, 88, 16, 89, 23, 59, 35, 89], [41, 97, 22, 74, 1, 46, 22, 32, 87, 30, 87, 43, 12, 83, 71, 27, 26, 18, 92, 75, 66, 81, 61, 46, 29, 32, 15, 60, 82, 28, 27, 41, 47, 33, 44, 50], [10, 24, 34, 91, 20, 25, 55, 90, 43, 53, 85, 50, 55, 13, 49, 97, 10, 92, 97, 11, 78, 84, 20, 72, 79, 97, 83, 48, 76, 17, 33, 20, 46, 31, 51, 83], [19, 62, 44, 77, 38, 49, 65, 11, 27, 58, 64, 65, 15, 82, 89, 1, 19, 56, 64, 34, 64, 10, 76, 60, 39, 66, 32, 51, 26, 57, 84, 60, 55, 6, 7, 66], [81, 26, 95, 98, 82, 78, 5, 87, 1, 84, 2, 65, 10, 50, 51, 69, 41, 58, 77, 68, 24, 91, 56, 36, 2, 96, 56, 81, 12, 12, 85, 72, 22, 74, 84, 62], [64, 28, 89, 28, 4, 45, 90, 13, 83, 98, 80, 4, 61, 84, 26, 94, 6, 77, 56, 81, 27, 35, 97, 82, 58, 84, 63, 33, 95, 83, 97, 81, 33, 69, 40, 47], [45, 27, 7, 58, 14, 4, 82, 34, 80, 91, 38, 20, 46, 19, 1, 23, 62, 73, 28, 84, 80, 77, 33, 3, 79, 16, 30, 25, 78, 1, 33, 37, 29, 37, 61, 8], [1, 63, 88, 65, 46, 43, 10, 82, 85, 10, 62, 86, 51, 45, 73, 73, 45, 85, 58, 95, 66, 24, 97, 75, 65, 55, 51, 72, 73, 21, 47, 22, 29, 40, 3, 49], [25, 82, 11, 94, 89, 75, 98, 88, 48, 32, 3, 45, 89, 20, 20, 51, 81, 20, 82, 14, 98, 80, 32, 72, 42, 80, 39, 38, 64, 4, 99, 92, 63, 61, 78, 5], [66, 45, 50, 88, 3, 23, 11, 38, 56, 35, 65, 6, 70, 40, 90, 35, 13, 25, 86, 81, 78, 67, 68, 99, 47, 55, 92, 43, 2, 45, 48, 62, 38, 47, 4, 60], [49, 76, 34, 44, 94, 85, 56, 92, 42, 50, 69, 33, 98, 96, 91, 67, 42, 44, 68, 57, 36, 41, 56, 3, 56, 56, 65, 39, 40, 39, 27, 67, 94, 65, 74, 3], [3, 37, 98, 20, 11, 83, 91, 24, 70, 65, 83, 74, 32, 62, 55, 36, 66, 37, 14, 46, 77, 56, 50, 61, 17, 27, 54, 29, 13, 49, 25, 88, 23, 26, 48, 36], [6, 80, 74, 39, 57, 91, 66, 10, 72, 9, 77, 72, 27, 46, 63, 42, 85, 41, 34, 93, 30, 44, 80, 1, 45, 47, 93, 30, 22, 15, 84, 38, 23, 31, 57, 81], [35, 66, 53, 31, 26, 31, 72, 80, 12, 53, 56, 83, 62, 44, 58, 77, 65, 13, 61, 68, 51, 62, 48, 95, 63, 72, 91, 72, 51, 24, 86, 40, 29, 73, 17, 1], [96, 84, 1, 25, 41, 91, 23, 18, 95, 28, 85, 12, 88, 49, 97, 81, 97, 16, 27, 53, 92, 36, 7, 34, 65, 4, 26, 20, 51, 77, 99, 10, 8, 18, 17, 69], [30, 95, 39, 61, 24, 81, 98, 35, 79, 61, 75, 98, 72, 15, 36, 55, 37, 87, 62, 64, 39, 90, 98, 75, 12, 72, 8, 41, 69, 74, 3, 43, 37, 86, 57, 25], [4, 58, 37, 8, 94, 9, 79, 1, 13, 68, 16, 44, 65, 14, 91, 26, 32, 2, 16, 92, 49, 90, 75, 23, 94, 60, 95, 66, 20, 93, 74, 18, 59, 31, 4, 27]],35,),
    ([[95, 71, 19, 39, 66, 78, 46, 92, 38, 67, 29, 91, 57, 48, 52, 48, 61, 67, 48, 94, 82, 8, 74, 86, 88, 67, 14, 47, 24, 91, 62, 58, 34, 31, 48, 91, 45, 29, 29, 63, 48, 12, 78, 27], [47, 66, 37, 45, 57, 18, 13, 73, 29, 56, 74, 20, 29, 6, 26, 61, 86, 43, 47, 26, 81, 1, 95, 73, 26, 64, 62, 6, 62, 66, 42, 27, 65, 30, 82, 98, 85, 65, 47, 32, 34, 47, 14, 5], [36, 96, 9, 35, 25, 75, 46, 13, 61, 30, 98, 32, 30, 82, 56, 67, 71, 55, 98, 8, 43, 48, 58, 32, 78, 69, 7, 74, 20, 62, 21, 92, 29, 70, 38, 42, 3, 37, 17, 33, 10, 37, 33, 28], [87, 42, 58, 48, 51, 10, 8, 16, 96, 62, 49, 89, 15, 16, 81, 27, 47, 26, 72, 41, 11, 91, 9, 54, 11, 7, 28, 94, 62, 55, 36, 73, 99, 63, 51, 77, 48, 68, 10, 26, 67, 53, 43, 17], [27, 22, 36, 72, 33, 90, 95, 53, 11, 93, 29, 38, 58, 15, 54, 62, 57, 79, 71, 58, 49, 53, 29, 33, 46, 54, 80, 98, 85, 7, 29, 9, 49, 71, 78, 94, 88, 51, 98, 8, 55, 65, 98, 84], [95, 79, 15, 51, 34, 69, 86, 12, 45, 31, 54, 93, 22, 72, 64, 60, 28, 21, 75, 75, 87, 77, 43, 27, 23, 97, 90, 36, 97, 38, 16, 74, 43, 41, 44, 52, 17, 52, 43, 23, 1, 93, 25, 6], [74, 54, 78, 23, 19, 56, 53, 31, 38, 19, 1, 77, 50, 98, 58, 81, 32, 49, 98, 97, 92, 44, 29, 88, 48, 80, 77, 26, 7, 44, 14, 52, 32, 75, 32, 75, 84, 57, 52, 34, 61, 62, 86, 87], [93, 76, 31, 29, 31, 12, 35, 57, 41, 27, 15, 94, 71, 36, 24, 82, 24, 96, 76, 28, 75, 3, 3, 29, 32, 54, 38, 95, 56, 65, 21, 41, 20, 60, 75, 59, 74, 55, 3, 14, 45, 95, 99, 60], [49, 9, 54, 70, 93, 52, 63, 52, 22, 55, 3, 2, 59, 28, 37, 69, 9, 62, 32, 81, 75, 35, 47, 18, 36, 19, 25, 46, 60, 95, 23, 78, 27, 35, 77, 55, 36, 88, 97, 71, 9, 21, 32, 66], [44, 89, 65, 75, 80, 87, 15, 27, 16, 46, 97, 72, 48, 65, 19, 90, 37, 58, 55, 53, 47, 3, 88, 86, 62, 1, 39, 73, 33, 23, 34, 49, 49, 99, 49, 10, 96, 66, 71, 88, 67, 76, 39, 42], [91, 1, 46, 36, 96, 91, 44, 31, 97, 58, 96, 4, 53, 89, 93, 57, 73, 78, 50, 5, 52, 17, 32, 6, 69, 93, 92, 61, 10, 23, 53, 61, 19, 4, 46, 32, 84, 46, 62, 92, 54, 87, 67, 24], [66, 18, 96, 48, 46, 48, 62, 94, 27, 62, 78, 65, 52, 1, 50, 40, 72, 17, 1, 78, 77, 30, 77, 67, 22, 35, 56, 14, 45, 86, 33, 12, 24, 69, 57, 9, 2, 59, 95, 29, 93, 55, 94, 22], [85, 49, 12, 71, 89, 8, 97, 16, 40, 45, 64, 63, 51, 10, 76, 86, 71, 45, 85, 56, 86, 73, 84, 13, 64, 88, 30, 52, 54, 57, 18, 25, 53, 20, 11, 40, 98, 23, 90, 87, 42, 47, 56, 33], [89, 98, 26, 69, 29, 94, 60, 91, 37, 25, 74, 44, 34, 12, 93, 39, 19, 19, 29, 66, 90, 98, 94, 76, 20, 57, 97, 9, 2, 28, 34, 21, 83, 78, 81, 56, 5, 85, 22, 59, 40, 84, 92, 63], [32, 45, 83, 92, 87, 33, 82, 35, 46, 36, 62, 83, 90, 26, 7, 87, 5, 87, 32, 79, 91, 81, 84, 57, 80, 62, 28, 95, 80, 78, 74, 66, 97, 41, 86, 66, 64, 7, 41, 45, 44, 30, 38, 39], [19, 47, 38, 17, 74, 79, 69, 99, 4, 35, 1, 81, 85, 58, 22, 5, 60, 36, 9, 84, 57, 78, 84, 90, 4, 51, 39, 84, 52, 75, 71, 55, 31, 50, 8, 87, 15, 65, 10, 41, 88, 79, 48, 21], [86, 24, 74, 23, 80, 69, 33, 36, 25, 58, 90, 66, 98, 31, 44, 63, 45, 83, 82, 50, 67, 71, 87, 1, 71, 86, 67, 83, 94, 9, 99, 35, 13, 26, 45, 51, 92, 25, 56, 39, 3, 75, 94, 53], [33, 62, 98, 67, 69, 95, 4, 72, 59, 17, 22, 38, 88, 31, 49, 52, 89, 38, 96, 49, 90, 27, 23, 84, 27, 81, 14, 3, 27, 62, 14, 92, 44, 25, 61, 75, 52, 12, 97, 84, 34, 23, 19, 1], [74, 65, 5, 57, 22, 43, 2, 73, 7, 21, 71, 59, 9, 40, 73, 49, 12, 73, 10, 74, 17, 4, 64, 16, 49, 27, 6, 9, 58, 32, 38, 30, 78, 45, 29, 92, 22, 31, 81, 17, 54, 79, 47, 32], [28, 11, 39, 17, 76, 39, 73, 25, 26, 68, 62, 19, 13, 29, 54, 73, 42, 62, 71, 71, 21, 9, 45, 27, 48, 85, 69, 5, 72, 15, 77, 97, 44, 47, 32, 36, 49, 53, 23, 34, 18, 12, 87, 2], [27, 50, 31, 48, 86, 69, 17, 43, 71, 18, 66, 31, 63, 28, 67, 9, 97, 28, 92, 18, 15, 75, 89, 5, 41, 91, 76, 74, 73, 66, 73, 51, 16, 65, 85, 57, 37, 39, 65, 49, 47, 40, 14, 40], [48, 32, 88, 39, 33, 30, 26, 43, 55, 44, 78, 76, 3, 7, 85, 58, 91, 10, 10, 81, 42, 34, 82, 26, 60, 2, 73, 45, 5, 26, 79, 25, 26, 92, 87, 85, 22, 19, 10, 42, 31, 31, 99, 75], [81, 97, 86, 90, 36, 66, 32, 67, 63, 23, 50, 65, 69, 44, 58, 57, 37, 65, 18, 5, 82, 99, 96, 26, 33, 42, 88, 27, 54, 83, 82, 79, 91, 75, 24, 3, 39, 71, 12, 33, 22, 35, 14, 26], [83, 85, 54, 41, 45, 31, 69, 99, 17, 60, 96, 4, 10, 94, 9, 61, 90, 22, 21, 23, 61, 12, 95, 17, 55, 21, 54, 47, 41, 97, 15, 96, 59, 99, 15, 29, 11, 29, 86, 90, 82, 89, 85, 88], [56, 92, 53, 3, 13, 38, 70, 11, 23, 73, 56, 17, 9, 83, 99, 96, 92, 28, 79, 19, 97, 87, 92, 4, 47, 47, 31, 99, 5, 33, 48, 32, 79, 59, 98, 64, 47, 9, 35, 47, 88, 82, 17, 1], [55, 11, 33, 70, 56, 64, 93, 58, 20, 18, 78, 45, 43, 20, 57, 82, 27, 18, 17, 60, 89, 5, 6, 97, 15, 39, 80, 39, 88, 21, 13, 29, 98, 5, 67, 21, 9, 67, 44, 62, 94, 67, 62, 62], [60, 49, 39, 41, 50, 98, 17, 53, 55, 78, 75, 56, 1, 65, 64, 52, 15, 2, 12, 45, 57, 42, 2, 87, 62, 34, 17, 41, 78, 75, 84, 71, 65, 15, 38, 98, 73, 65, 9, 42, 66, 86, 89, 51], [78, 99, 80, 19, 31, 66, 32, 75, 8, 69, 98, 32, 47, 70, 8, 34, 4, 36, 44, 25, 26, 33, 9, 47, 72, 17, 15, 42, 54, 13, 50, 44, 3, 53, 56, 54, 57, 12, 93, 59, 65, 96, 37, 20], [72, 37, 31, 95, 25, 50, 49, 8, 94, 94, 91, 35, 13, 21, 73, 24, 48, 33, 1, 72, 3, 14, 14, 49, 33, 4, 38, 25, 47, 13, 39, 25, 73, 43, 38, 35, 93, 55, 50, 78, 34, 25, 42, 92], [51, 94, 37, 66, 85, 34, 83, 38, 31, 26, 76, 94, 26, 63, 48, 95, 79, 10, 36, 40, 26, 9, 53, 81, 70, 86, 80, 86, 53, 39, 61, 52, 68, 68, 73, 78, 42, 90, 67, 96, 75, 51, 3, 13], [13, 61, 24, 20, 74, 87, 97, 55, 35, 78, 80, 30, 83, 33, 41, 66, 49, 8, 84, 3, 85, 65, 85, 72, 2, 87, 41, 53, 75, 16, 9, 96, 39, 64, 36, 23, 47, 49, 55, 94, 10, 63, 95, 26], [48, 30, 2, 29, 54, 32, 38, 21, 27, 88, 34, 23, 78, 39, 69, 73, 45, 63, 8, 7, 30, 12, 20, 64, 29, 55, 12, 84, 22, 23, 48, 45, 26, 28, 55, 73, 69, 2, 28, 77, 79, 53, 14, 46], [78, 67, 74, 70, 20, 35, 48, 43, 20, 56, 3, 68, 11, 62, 61, 95, 58, 29, 38, 84, 88, 87, 22, 86, 41, 84, 63, 38, 50, 7, 24, 46, 25, 78, 29, 67, 93, 80, 85, 22, 85, 86, 9, 87], [49, 73, 96, 36, 5, 90, 4, 24, 41, 14, 91, 12, 82, 44, 9, 66, 38, 96, 77, 57, 47, 55, 88, 2, 83, 18, 66, 90, 57, 64, 88, 27, 53, 59, 29, 72, 95, 98, 14, 68, 43, 29, 57, 33], [21, 41, 1, 27, 2, 64, 51, 54, 74, 74, 30, 1, 95, 99, 29, 13, 73, 43, 41, 75, 88, 89, 58, 77, 14, 41, 67, 54, 6, 46, 77, 1, 29, 78, 76, 26, 58, 87, 3, 60, 14, 98, 23, 62], [10, 4, 39, 74, 88, 34, 88, 25, 52, 15, 12, 1, 9, 59, 14, 31, 88, 53, 63, 10, 43, 18, 67, 59, 76, 99, 23, 86, 75, 46, 49, 23, 12, 29, 89, 88, 59, 53, 68, 63, 29, 3, 95, 89], [37, 63, 23, 49, 86, 93, 77, 3, 22, 36, 10, 9, 56, 55, 19, 72, 33, 20, 94, 35, 31, 83, 50, 46, 78, 10, 67, 34, 51, 92, 83, 39, 90, 68, 12, 26, 71, 67, 90, 2, 12, 59, 32, 51], [11, 32, 64, 45, 79, 54, 6, 26, 8, 8, 38, 8, 17, 83, 3, 41, 73, 53, 97, 96, 96, 70, 62, 53, 59, 93, 81, 83, 95, 83, 23, 47, 35, 14, 65, 97, 49, 36, 1, 84, 22, 35, 3, 12], [37, 58, 77, 12, 2, 84, 65, 58, 60, 41, 35, 88, 90, 11, 52, 52, 62, 63, 15, 70, 40, 9, 70, 17, 23, 58, 95, 80, 51, 57, 86, 16, 45, 61, 12, 73, 6, 4, 81, 74, 35, 47, 85, 19], [27, 11, 70, 59, 41, 43, 28, 63, 67, 45, 24, 77, 64, 79, 73, 39, 99, 45, 61, 82, 43, 67, 92, 80, 42, 41, 47, 43, 23, 32, 74, 57, 38, 77, 15, 28, 13, 35, 2, 61, 65, 41, 96, 94], [86, 4, 53, 88, 14, 17, 14, 41, 62, 52, 27, 85, 40, 35, 90, 95, 59, 97, 49, 63, 11, 80, 6, 98, 41, 32, 21, 93, 75, 57, 5, 91, 28, 95, 75, 77, 70, 27, 94, 53, 48, 83, 78, 58], [9, 55, 45, 28, 28, 46, 25, 26, 62, 68, 67, 34, 21, 81, 34, 44, 76, 89, 21, 18, 36, 70, 84, 53, 20, 96, 95, 84, 94, 3, 84, 8, 85, 48, 23, 1, 2, 74, 37, 94, 51, 44, 24, 32], [56, 50, 64, 30, 38, 78, 55, 3, 25, 45, 62, 7, 81, 27, 23, 32, 2, 75, 34, 52, 61, 34, 7, 10, 89, 2, 30, 81, 29, 82, 60, 99, 17, 56, 86, 51, 25, 84, 16, 25, 15, 79, 57, 15], [56, 82, 37, 65, 33, 3, 49, 22, 54, 21, 27, 4, 99, 1, 4, 55, 24, 29, 22, 23, 85, 78, 8, 58, 80, 99, 88, 59, 90, 7, 25, 45, 90, 26, 30, 66, 53, 73, 39, 11, 79, 12, 99, 50]],29,),
    ([[16, 49, 32, 82, 45, 85, 80, 71, 5, 44, 41, 97, 95, 85, 67, 74, 75, 22, 17, 89, 92, 50, 84, 94, 31, 13, 74, 51, 33, 20, 48, 78, 72, 72, 92, 74, 14, 62, 51, 78, 70, 98, 81, 21, 92, 38, 15], [36, 9, 99, 59, 82, 54, 17, 82, 4, 84, 13, 75, 43, 97, 92, 8, 20, 82, 71, 61, 44, 97, 51, 58, 75, 30, 99, 84, 10, 94, 18, 25, 96, 34, 44, 39, 95, 92, 90, 68, 43, 20, 72, 2, 27, 34, 55], [36, 85, 72, 87, 72, 69, 65, 85, 44, 43, 74, 66, 21, 61, 13, 28, 30, 82, 2, 58, 83, 21, 90, 46, 89, 83, 25, 57, 20, 6, 18, 49, 82, 20, 34, 10, 33, 55, 19, 66, 47, 49, 67, 30, 83, 85, 59], [78, 31, 21, 17, 53, 51, 24, 40, 98, 47, 20, 16, 58, 49, 42, 12, 41, 58, 60, 24, 13, 34, 61, 27, 85, 67, 14, 41, 57, 30, 45, 74, 1, 92, 83, 94, 84, 52, 20, 23, 95, 96, 90, 78, 6, 33, 8], [63, 4, 13, 35, 93, 89, 34, 56, 11, 38, 93, 45, 86, 58, 34, 75, 92, 72, 24, 74, 79, 63, 39, 21, 36, 48, 84, 13, 2, 27, 7, 90, 94, 19, 40, 21, 58, 26, 74, 36, 44, 64, 27, 8, 90, 1, 23], [73, 31, 7, 9, 71, 92, 98, 53, 16, 74, 24, 74, 46, 29, 89, 30, 51, 83, 31, 30, 34, 92, 19, 75, 28, 6, 17, 91, 36, 1, 16, 68, 47, 23, 96, 67, 62, 85, 88, 15, 75, 67, 83, 43, 8, 98, 98], [44, 26, 67, 32, 64, 43, 74, 74, 62, 11, 78, 95, 9, 48, 6, 54, 62, 54, 99, 98, 56, 82, 87, 30, 3, 61, 15, 3, 15, 67, 29, 31, 71, 71, 55, 75, 92, 43, 25, 81, 55, 50, 38, 60, 85, 52, 84], [74, 70, 76, 81, 45, 97, 19, 5, 42, 93, 30, 65, 76, 79, 5, 38, 11, 84, 29, 14, 90, 98, 74, 91, 89, 10, 39, 60, 96, 98, 23, 97, 96, 22, 86, 87, 83, 23, 22, 62, 94, 19, 22, 1, 34, 26, 4], [48, 45, 12, 92, 37, 3, 28, 93, 84, 2, 56, 65, 46, 44, 18, 73, 37, 54, 25, 83, 62, 25, 52, 63, 15, 46, 56, 26, 64, 20, 67, 25, 21, 34, 88, 25, 65, 29, 32, 1, 35, 56, 16, 32, 79, 5, 10], [86, 72, 79, 20, 89, 12, 90, 68, 63, 26, 60, 74, 61, 15, 5, 32, 96, 22, 22, 12, 64, 75, 88, 80, 16, 65, 51, 87, 92, 32, 53, 3, 13, 92, 92, 58, 45, 24, 51, 13, 24, 5, 81, 50, 76, 49, 18], [33, 58, 31, 34, 94, 96, 74, 31, 99, 79, 27, 59, 27, 1, 76, 68, 23, 98, 52, 57, 87, 51, 83, 84, 63, 84, 93, 77, 28, 24, 22, 86, 40, 75, 8, 96, 88, 12, 49, 21, 67, 39, 62, 82, 58, 62, 70], [36, 45, 79, 15, 62, 38, 64, 88, 71, 9, 75, 80, 71, 25, 78, 65, 20, 28, 49, 34, 73, 20, 95, 85, 22, 77, 44, 47, 25, 22, 61, 52, 20, 96, 80, 20, 86, 45, 37, 15, 76, 9, 44, 15, 44, 86, 12], [27, 19, 25, 74, 99, 64, 12, 50, 72, 11, 83, 23, 88, 15, 63, 20, 89, 78, 10, 61, 93, 47, 49, 49, 76, 33, 87, 78, 23, 53, 37, 22, 93, 2, 20, 5, 91, 3, 82, 77, 86, 77, 12, 32, 58, 71, 70], [40, 6, 63, 25, 91, 69, 83, 73, 50, 40, 1, 46, 73, 39, 10, 49, 14, 46, 40, 89, 19, 17, 82, 46, 73, 65, 70, 38, 17, 73, 11, 53, 18, 7, 35, 44, 71, 39, 11, 10, 98, 88, 76, 9, 86, 96, 8], [48, 21, 80, 97, 89, 6, 59, 68, 23, 73, 75, 35, 12, 99, 71, 57, 29, 85, 67, 61, 61, 88, 30, 27, 93, 30, 55, 23, 37, 26, 36, 92, 63, 37, 51, 68, 93, 78, 63, 37, 97, 31, 78, 25, 73, 25, 46], [89, 30, 20, 23, 1, 15, 21, 30, 11, 90, 52, 30, 9, 69, 47, 34, 33, 98, 65, 51, 79, 31, 56, 76, 71, 45, 33, 96, 51, 5, 38, 5, 56, 81, 71, 89, 25, 67, 52, 36, 92, 23, 8, 31, 63, 21, 99], [50, 29, 60, 67, 44, 89, 2, 98, 15, 39, 40, 47, 76, 52, 88, 6, 70, 48, 58, 90, 3, 96, 46, 18, 56, 92, 33, 17, 32, 76, 85, 2, 26, 39, 63, 17, 34, 19, 62, 32, 50, 86, 45, 54, 82, 88, 1], [66, 40, 24, 52, 2, 61, 27, 66, 87, 33, 34, 62, 32, 3, 55, 27, 76, 8, 20, 52, 17, 33, 55, 75, 73, 98, 71, 16, 91, 79, 64, 88, 40, 58, 83, 23, 95, 94, 7, 59, 59, 3, 30, 10, 98, 13, 39], [77, 64, 25, 41, 98, 40, 62, 40, 34, 79, 3, 52, 46, 86, 98, 69, 41, 86, 60, 29, 8, 98, 4, 25, 50, 23, 25, 98, 70, 98, 21, 94, 56, 3, 79, 21, 83, 83, 49, 46, 98, 78, 68, 31, 46, 75, 44], [45, 75, 49, 4, 80, 57, 56, 38, 6, 82, 89, 24, 52, 39, 73, 37, 98, 34, 40, 40, 37, 92, 50, 11, 78, 59, 26, 60, 8, 28, 84, 60, 89, 10, 63, 61, 75, 26, 23, 63, 19, 18, 50, 19, 15, 16, 20], [19, 75, 71, 19, 88, 31, 52, 48, 8, 50, 61, 88, 8, 13, 74, 19, 50, 23, 57, 97, 30, 94, 29, 61, 35, 9, 72, 25, 64, 37, 38, 8, 90, 75, 40, 23, 96, 45, 1, 49, 9, 40, 28, 97, 96, 8, 37], [82, 71, 18, 76, 68, 77, 75, 80, 44, 78, 16, 52, 53, 86, 18, 40, 61, 25, 35, 71, 84, 27, 93, 10, 75, 20, 33, 77, 80, 11, 69, 67, 59, 66, 53, 38, 10, 6, 85, 95, 34, 49, 32, 29, 65, 33, 17], [98, 49, 16, 7, 13, 84, 4, 63, 69, 80, 73, 76, 78, 15, 5, 42, 18, 72, 8, 89, 68, 26, 75, 70, 33, 22, 93, 69, 1, 86, 35, 56, 95, 67, 3, 71, 1, 42, 58, 88, 94, 96, 96, 85, 64, 80, 4], [17, 77, 99, 40, 34, 56, 11, 89, 40, 94, 13, 24, 34, 8, 82, 7, 62, 46, 86, 71, 13, 2, 2, 29, 91, 82, 58, 2, 59, 53, 68, 61, 49, 46, 72, 59, 48, 9, 18, 50, 86, 75, 27, 32, 66, 66, 94], [22, 86, 24, 91, 75, 13, 91, 15, 49, 17, 39, 73, 87, 4, 57, 15, 43, 31, 6, 90, 59, 65, 86, 30, 58, 86, 97, 56, 69, 36, 46, 74, 1, 12, 67, 10, 1, 19, 82, 95, 55, 49, 55, 86, 68, 41, 55], [74, 74, 79, 69, 43, 81, 82, 57, 48, 50, 69, 8, 56, 91, 89, 26, 23, 41, 87, 93, 97, 59, 18, 71, 96, 71, 8, 58, 85, 17, 51, 33, 30, 66, 60, 46, 22, 32, 25, 8, 97, 63, 29, 81, 40, 45, 2], [49, 31, 68, 90, 9, 95, 10, 51, 70, 44, 26, 75, 79, 84, 78, 21, 91, 30, 71, 15, 80, 59, 84, 84, 86, 70, 20, 69, 53, 75, 2, 30, 8, 40, 8, 17, 99, 30, 1, 69, 64, 80, 36, 79, 49, 81, 77], [24, 4, 77, 62, 9, 26, 47, 16, 37, 70, 11, 2, 94, 83, 23, 47, 62, 76, 39, 6, 36, 62, 60, 79, 36, 77, 72, 89, 88, 31, 40, 60, 13, 93, 96, 37, 61, 18, 90, 18, 34, 54, 31, 79, 37, 84, 92], [68, 72, 58, 82, 96, 53, 87, 62, 79, 7, 31, 96, 40, 78, 83, 50, 80, 9, 65, 25, 8, 39, 32, 8, 13, 67, 66, 28, 4, 23, 34, 55, 71, 94, 58, 73, 19, 9, 23, 75, 13, 93, 31, 72, 19, 5, 91], [39, 14, 22, 22, 5, 62, 52, 80, 39, 26, 80, 56, 12, 80, 49, 12, 96, 5, 92, 51, 4, 93, 83, 25, 99, 24, 56, 19, 23, 95, 83, 96, 77, 46, 18, 61, 71, 45, 88, 46, 17, 15, 73, 34, 99, 8, 50], [11, 88, 42, 94, 85, 43, 35, 59, 12, 73, 12, 28, 93, 46, 40, 99, 29, 70, 16, 46, 92, 65, 29, 52, 40, 6, 27, 37, 22, 7, 1, 77, 48, 51, 14, 79, 12, 49, 41, 68, 85, 2, 85, 62, 57, 14, 44], [66, 75, 37, 78, 47, 61, 84, 99, 27, 49, 60, 70, 71, 45, 1, 13, 38, 17, 38, 1, 1, 83, 30, 77, 7, 20, 44, 73, 13, 39, 20, 89, 5, 52, 25, 12, 90, 56, 86, 1, 72, 49, 67, 22, 85, 85, 31], [1, 27, 2, 93, 1, 42, 8, 35, 35, 7, 23, 23, 46, 19, 79, 72, 97, 99, 13, 50, 31, 71, 84, 38, 57, 8, 14, 94, 51, 9, 13, 76, 66, 38, 21, 29, 84, 50, 64, 9, 15, 53, 97, 53, 71, 3, 87], [22, 39, 77, 9, 34, 12, 34, 45, 97, 50, 99, 28, 39, 3, 47, 12, 43, 77, 67, 18, 90, 10, 4, 12, 53, 51, 16, 17, 95, 26, 2, 29, 94, 47, 11, 34, 71, 29, 97, 49, 91, 16, 81, 75, 14, 13, 35], [90, 52, 25, 59, 76, 68, 42, 48, 91, 45, 72, 72, 29, 3, 21, 31, 13, 95, 81, 48, 96, 24, 2, 3, 26, 2, 33, 34, 90, 98, 38, 78, 95, 20, 10, 84, 33, 45, 60, 66, 61, 51, 12, 80, 9, 11, 21], [76, 68, 26, 63, 19, 17, 44, 61, 1, 72, 58, 94, 41, 24, 43, 81, 94, 9, 66, 90, 32, 91, 41, 11, 65, 18, 8, 27, 82, 9, 2, 81, 75, 46, 70, 5, 12, 44, 42, 99, 88, 30, 52, 81, 47, 36, 70], [32, 98, 44, 16, 71, 96, 17, 32, 14, 26, 73, 13, 89, 12, 45, 16, 94, 52, 21, 24, 43, 5, 33, 31, 9, 35, 8, 75, 17, 80, 20, 91, 78, 22, 54, 71, 75, 81, 77, 81, 75, 68, 80, 31, 85, 97, 13], [29, 79, 10, 33, 15, 77, 35, 54, 21, 30, 46, 42, 71, 49, 24, 80, 69, 6, 2, 3, 53, 10, 24, 33, 84, 22, 61, 96, 94, 67, 4, 51, 4, 39, 31, 57, 73, 30, 93, 89, 39, 99, 25, 58, 36, 11, 90], [46, 89, 21, 2, 74, 39, 99, 33, 31, 4, 67, 69, 81, 13, 65, 45, 39, 87, 89, 53, 31, 13, 1, 98, 29, 61, 95, 72, 2, 12, 56, 97, 94, 41, 27, 89, 38, 97, 52, 80, 32, 88, 2, 66, 20, 57, 62], [91, 86, 48, 83, 7, 67, 50, 34, 87, 69, 67, 88, 91, 34, 43, 21, 12, 32, 47, 86, 98, 87, 55, 65, 68, 17, 26, 95, 33, 64, 92, 10, 46, 73, 90, 51, 34, 14, 41, 90, 95, 38, 48, 43, 28, 41, 56], [81, 76, 91, 65, 60, 97, 13, 69, 52, 43, 92, 88, 84, 40, 42, 37, 84, 23, 67, 69, 79, 69, 98, 58, 46, 87, 47, 17, 9, 68, 94, 78, 30, 95, 61, 65, 58, 27, 66, 45, 40, 61, 41, 74, 88, 84, 42], [62, 80, 38, 60, 49, 18, 99, 94, 5, 11, 4, 61, 75, 12, 49, 28, 90, 34, 56, 65, 6, 33, 47, 24, 34, 72, 16, 80, 16, 98, 84, 14, 59, 62, 90, 66, 19, 61, 66, 26, 89, 49, 19, 49, 81, 30, 76], [57, 85, 36, 40, 28, 97, 46, 73, 82, 88, 32, 87, 58, 76, 98, 26, 70, 69, 87, 50, 79, 32, 58, 64, 77, 28, 97, 72, 80, 39, 96, 80, 45, 13, 20, 58, 19, 75, 91, 80, 9, 77, 19, 94, 55, 39, 17], [62, 94, 93, 60, 42, 2, 50, 67, 20, 1, 5, 97, 39, 87, 18, 68, 97, 90, 22, 30, 90, 1, 70, 81, 95, 51, 68, 74, 61, 48, 53, 34, 86, 86, 7, 39, 37, 63, 55, 15, 83, 74, 62, 68, 50, 41, 61], [25, 28, 82, 35, 83, 53, 84, 39, 97, 59, 65, 1, 45, 19, 48, 49, 73, 14, 67, 30, 65, 69, 87, 6, 84, 46, 42, 72, 61, 31, 79, 26, 58, 33, 52, 32, 54, 1, 5, 22, 95, 5, 8, 70, 63, 10, 62], [40, 47, 80, 56, 28, 56, 1, 52, 82, 62, 42, 47, 37, 11, 67, 29, 4, 95, 11, 30, 79, 79, 58, 32, 29, 43, 92, 85, 39, 11, 96, 27, 24, 37, 65, 32, 53, 1, 56, 34, 82, 29, 6, 57, 95, 14, 75], [69, 62, 86, 51, 13, 76, 4, 38, 4, 30, 54, 65, 61, 49, 31, 42, 50, 23, 78, 99, 81, 60, 32, 56, 56, 87, 34, 41, 39, 86, 42, 66, 20, 14, 38, 37, 37, 12, 92, 56, 8, 93, 21, 39, 48, 18, 63]],41,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))