# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( mat , n ) :
    tot_energy = 0
    for i in range ( n ) :
        for j in range ( n ) :
            q = mat [ i ] [ j ] // n
            i_des = q
            j_des = mat [ i ] [ j ] - ( n * q )
            tot_energy += ( abs ( i_des - i ) + abs ( j_des - j ) )
    return tot_energy


#TOFILL

if __name__ == '__main__':
    param = [
    ([[4, 7, 10, 11, 14, 22, 27, 43, 45, 47, 48, 48, 49, 49, 51, 54, 56, 57, 59, 62, 63, 64, 66, 79, 82, 83, 87, 96, 97, 97, 98], [1, 1, 10, 13, 14, 18, 31, 33, 35, 37, 37, 42, 43, 44, 46, 54, 60, 61, 63, 63, 67, 67, 74, 76, 81, 83, 88, 91, 91, 96, 97], [2, 3, 4, 10, 11, 13, 17, 27, 30, 35, 35, 38, 39, 44, 47, 52, 52, 60, 61, 65, 68, 69, 71, 75, 76, 76, 85, 93, 94, 94, 98], [3, 5, 5, 19, 22, 23, 24, 24, 27, 31, 31, 32, 32, 44, 46, 50, 52, 54, 55, 57, 58, 59, 61, 61, 68, 72, 76, 78, 79, 85, 98], [7, 10, 14, 15, 21, 28, 30, 31, 40, 46, 51, 51, 52, 54, 57, 58, 58, 64, 67, 68, 68, 71, 72, 76, 79, 80, 85, 88, 88, 91, 93], [2, 5, 18, 21, 21, 25, 28, 31, 33, 34, 37, 38, 42, 45, 47, 56, 64, 70, 71, 75, 76, 78, 78, 81, 84, 88, 90, 91, 98, 98, 99], [10, 11, 14, 17, 18, 22, 27, 35, 36, 37, 46, 53, 55, 59, 59, 64, 66, 66, 66, 69, 69, 73, 73, 74, 74, 85, 86, 87, 89, 93, 99], [11, 13, 13, 14, 17, 18, 19, 19, 21, 25, 25, 29, 36, 36, 42, 43, 45, 49, 57, 61, 64, 65, 71, 75, 84, 84, 89, 94, 94, 95, 98], [1, 1, 2, 2, 10, 10, 21, 22, 23, 24, 24, 29, 34, 40, 46, 48, 49, 49, 50, 60, 73, 73, 75, 80, 81, 85, 86, 93, 96, 97, 99], [1, 2, 10, 15, 16, 18, 19, 21, 23, 25, 29, 29, 31, 31, 32, 38, 42, 43, 48, 51, 54, 56, 63, 74, 74, 74, 88, 88, 94, 94, 94], [19, 24, 25, 27, 29, 33, 34, 35, 36, 37, 37, 44, 45, 50, 51, 51, 52, 54, 59, 59, 66, 69, 70, 75, 77, 80, 81, 84, 97, 99, 99], [1, 2, 5, 5, 7, 12, 17, 19, 20, 38, 44, 45, 47, 48, 51, 55, 59, 61, 61, 64, 65, 67, 74, 76, 76, 77, 79, 83, 86, 92, 92], [3, 5, 5, 12, 18, 23, 25, 38, 38, 48, 49, 57, 61, 63, 67, 70, 71, 75, 75, 77, 78, 79, 80, 80, 84, 87, 92, 92, 95, 96, 98], [1, 3, 3, 5, 7, 8, 9, 13, 17, 21, 23, 36, 38, 39, 39, 41, 45, 57, 71, 72, 72, 73, 76, 79, 80, 82, 83, 87, 89, 97, 99], [9, 10, 13, 14, 14, 16, 17, 23, 26, 27, 28, 31, 32, 38, 38, 43, 45, 50, 51, 52, 52, 64, 66, 68, 71, 78, 85, 85, 85, 91, 91], [1, 2, 2, 3, 10, 12, 13, 15, 15, 21, 25, 26, 28, 34, 45, 45, 46, 46, 49, 49, 52, 55, 57, 61, 62, 63, 70, 72, 73, 84, 86], [5, 5, 8, 13, 16, 18, 21, 25, 29, 33, 35, 36, 39, 45, 46, 47, 49, 58, 66, 68, 70, 71, 77, 80, 83, 83, 86, 87, 94, 97, 98], [5, 9, 17, 20, 24, 27, 27, 27, 28, 30, 32, 32, 35, 39, 40, 43, 45, 52, 55, 56, 63, 71, 76, 78, 81, 86, 90, 95, 97, 98, 98], [1, 6, 6, 7, 15, 22, 29, 33, 38, 38, 42, 42, 44, 45, 53, 59, 61, 62, 62, 72, 75, 76, 77, 77, 80, 81, 89, 96, 96, 97, 99], [3, 4, 4, 10, 11, 12, 16, 17, 32, 33, 33, 36, 40, 40, 42, 42, 44, 45, 47, 52, 53, 56, 59, 62, 64, 67, 80, 80, 89, 90, 94], [2, 3, 8, 9, 15, 19, 20, 21, 22, 23, 23, 24, 24, 28, 28, 32, 36, 40, 43, 46, 54, 55, 65, 71, 76, 83, 86, 93, 93, 96, 97], [2, 3, 3, 4, 8, 11, 13, 14, 18, 19, 20, 22, 35, 39, 45, 60, 61, 64, 66, 69, 70, 70, 72, 72, 74, 75, 79, 83, 87, 90, 97], [19, 21, 22, 23, 24, 28, 30, 30, 32, 41, 42, 54, 56, 60, 62, 65, 71, 72, 72, 73, 75, 75, 78, 84, 85, 85, 85, 85, 87, 89, 92], [6, 7, 10, 11, 11, 16, 17, 20, 20, 23, 31, 33, 34, 36, 38, 42, 44, 48, 56, 57, 58, 63, 64, 69, 69, 70, 72, 81, 85, 89, 91], [9, 11, 13, 18, 21, 22, 24, 26, 26, 30, 35, 42, 51, 53, 55, 55, 58, 58, 59, 59, 61, 63, 67, 75, 79, 88, 88, 92, 96, 98, 99], [9, 12, 14, 17, 21, 21, 32, 35, 38, 39, 41, 43, 45, 45, 45, 55, 57, 57, 63, 67, 71, 72, 74, 75, 76, 77, 78, 83, 83, 85, 97], [3, 4, 13, 17, 20, 22, 28, 32, 36, 38, 39, 39, 52, 56, 60, 60, 61, 61, 62, 64, 65, 69, 71, 73, 82, 88, 91, 96, 96, 97, 99], [2, 2, 13, 14, 15, 19, 25, 32, 33, 34, 37, 38, 41, 45, 45, 53, 57, 59, 59, 60, 68, 71, 78, 80, 81, 84, 93, 93, 95, 99, 99], [5, 16, 17, 18, 18, 24, 27, 27, 32, 35, 41, 41, 49, 51, 56, 60, 60, 62, 67, 67, 71, 78, 78, 79, 82, 89, 92, 92, 95, 97, 98], [6, 7, 9, 10, 10, 12, 16, 19, 19, 26, 28, 31, 32, 33, 41, 43, 46, 47, 48, 49, 51, 52, 58, 66, 75, 75, 76, 78, 81, 88, 91], [8, 13, 18, 19, 22, 26, 26, 26, 27, 30, 30, 32, 33, 35, 35, 38, 45, 53, 57, 60, 63, 63, 65, 71, 77, 79, 81, 91, 96, 98, 99]],15,),
    ([[-40]],0,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],25,),
    ([[3, 86, 3, 43, 83, 22, 69, 67, 38, 82, 99, 59, 27, 2, 8, 84, 60, 93, 75, 37, 65, 79, 43, 69, 7, 42, 44, 77, 24, 58], [88, 63, 93, 78, 89, 63, 23, 39, 60, 17, 94, 68, 16, 76, 31, 4, 66, 91, 57, 98, 95, 83, 22, 79, 50, 34, 84, 59, 59, 39], [37, 36, 42, 78, 47, 20, 40, 18, 7, 56, 4, 26, 25, 64, 34, 28, 88, 46, 21, 45, 70, 75, 24, 29, 79, 7, 81, 32, 65, 87], [90, 25, 86, 26, 59, 67, 24, 74, 37, 68, 78, 5, 7, 15, 63, 20, 59, 90, 58, 50, 82, 19, 37, 64, 81, 74, 62, 3, 28, 87], [81, 75, 25, 44, 42, 86, 92, 29, 11, 50, 77, 77, 99, 69, 3, 49, 89, 35, 59, 95, 85, 51, 36, 72, 29, 74, 55, 72, 58, 16], [82, 37, 70, 98, 69, 84, 29, 36, 49, 94, 64, 72, 17, 95, 83, 51, 16, 65, 89, 21, 14, 4, 75, 99, 39, 60, 18, 65, 69, 6], [88, 1, 88, 12, 21, 19, 37, 85, 43, 80, 65, 79, 97, 12, 45, 12, 38, 62, 53, 21, 86, 67, 99, 12, 38, 83, 30, 32, 27, 29], [42, 25, 24, 59, 60, 38, 34, 96, 84, 77, 14, 97, 14, 1, 89, 95, 62, 57, 96, 59, 65, 52, 72, 70, 69, 36, 79, 34, 68, 33], [69, 92, 20, 1, 71, 47, 28, 33, 29, 80, 55, 67, 17, 82, 82, 68, 18, 24, 51, 49, 71, 62, 69, 36, 97, 39, 22, 97, 3, 63], [63, 34, 94, 31, 49, 43, 90, 61, 1, 55, 45, 29, 28, 13, 44, 26, 45, 14, 92, 96, 9, 39, 83, 53, 34, 59, 73, 52, 9, 28], [30, 46, 18, 73, 90, 38, 8, 49, 75, 15, 39, 10, 96, 85, 32, 53, 4, 93, 86, 7, 95, 87, 95, 59, 65, 22, 77, 79, 66, 30], [92, 28, 99, 32, 90, 28, 2, 97, 76, 97, 38, 39, 77, 84, 88, 19, 34, 23, 81, 81, 73, 13, 91, 68, 6, 21, 44, 30, 16, 2], [76, 7, 20, 53, 71, 29, 57, 33, 32, 53, 44, 25, 76, 28, 91, 15, 28, 14, 63, 78, 75, 49, 81, 93, 82, 45, 59, 81, 85, 97], [98, 10, 23, 21, 48, 22, 4, 43, 13, 24, 69, 62, 61, 11, 61, 95, 89, 31, 10, 77, 93, 41, 45, 32, 8, 42, 50, 15, 57, 10], [85, 90, 37, 19, 60, 33, 71, 96, 9, 10, 52, 20, 73, 67, 83, 18, 62, 19, 17, 43, 32, 15, 92, 47, 59, 83, 15, 45, 95, 90], [38, 86, 16, 5, 83, 44, 46, 23, 96, 75, 76, 15, 8, 58, 29, 81, 52, 30, 87, 45, 62, 82, 74, 69, 57, 99, 60, 13, 57, 92], [75, 52, 45, 6, 41, 30, 93, 17, 76, 53, 20, 13, 65, 38, 14, 51, 83, 93, 55, 83, 19, 81, 70, 57, 37, 95, 48, 52, 25, 86], [75, 79, 14, 80, 61, 82, 79, 70, 35, 31, 66, 47, 8, 2, 30, 96, 22, 94, 68, 59, 20, 29, 98, 14, 95, 33, 63, 72, 3, 1], [43, 21, 47, 66, 48, 27, 51, 75, 20, 87, 71, 98, 93, 4, 59, 22, 76, 65, 7, 38, 21, 26, 36, 86, 28, 78, 62, 98, 40, 5], [46, 57, 64, 58, 2, 92, 98, 82, 40, 87, 80, 96, 62, 53, 92, 27, 74, 38, 40, 72, 8, 81, 64, 25, 75, 54, 70, 91, 95, 42], [97, 97, 58, 63, 90, 72, 76, 74, 96, 96, 16, 43, 65, 97, 48, 95, 36, 16, 57, 38, 21, 11, 99, 39, 67, 61, 76, 89, 25, 83], [1, 5, 93, 79, 76, 93, 81, 74, 11, 6, 74, 49, 86, 23, 82, 24, 33, 65, 2, 49, 74, 6, 14, 11, 82, 32, 34, 41, 78, 5], [82, 67, 38, 85, 78, 83, 2, 93, 39, 17, 51, 17, 97, 99, 35, 98, 82, 84, 29, 68, 91, 86, 49, 16, 2, 50, 10, 34, 18, 45], [71, 44, 54, 31, 93, 84, 28, 82, 87, 53, 89, 45, 97, 23, 74, 76, 35, 4, 71, 92, 35, 68, 53, 2, 8, 38, 95, 68, 18, 6], [37, 28, 49, 99, 51, 64, 10, 80, 69, 45, 85, 58, 41, 56, 39, 67, 3, 77, 35, 75, 46, 44, 38, 70, 75, 19, 21, 91, 43, 78], [68, 31, 36, 20, 86, 37, 17, 3, 10, 68, 61, 59, 95, 80, 73, 52, 96, 23, 54, 33, 45, 74, 55, 83, 60, 55, 88, 59, 77, 9], [55, 81, 74, 8, 73, 6, 86, 64, 38, 76, 80, 62, 64, 11, 62, 72, 95, 22, 27, 57, 83, 85, 60, 36, 76, 28, 78, 24, 25, 80], [85, 85, 15, 8, 23, 92, 30, 74, 79, 90, 62, 20, 96, 61, 46, 80, 40, 7, 51, 27, 28, 43, 83, 39, 94, 10, 49, 98, 27, 84], [91, 70, 64, 86, 70, 85, 54, 69, 14, 67, 43, 22, 9, 91, 10, 84, 93, 3, 5, 87, 59, 54, 59, 82, 8, 73, 22, 33, 53, 64], [82, 37, 42, 38, 4, 98, 16, 82, 47, 87, 9, 34, 36, 92, 10, 72, 87, 72, 22, 40, 12, 96, 12, 30, 41, 18, 33, 37, 27, 45]],29,),
    ([[-96, -90, -78, -74, -70, -60, -52, -50, -48, -46, -32, -20, -20, -10, -6, -4, 4, 4, 6, 8, 8, 24, 32, 48, 48, 58, 86, 92, 98], [-68, -60, -58, -54, -40, -38, -22, -16, -16, -16, -12, 0, 4, 4, 30, 30, 42, 46, 48, 48, 50, 52, 52, 52, 66, 68, 76, 78, 96], [-92, -90, -86, -70, -60, -58, -48, -46, -46, -36, -34, -14, -14, -10, -2, 12, 44, 46, 52, 54, 66, 70, 70, 74, 76, 80, 86, 90, 98], [-98, -88, -78, -78, -74, -72, -68, -66, -66, -58, -36, -32, -26, -22, -6, -6, 8, 8, 18, 20, 22, 28, 34, 60, 70, 70, 70, 80, 90], [-98, -96, -96, -88, -86, -86, -72, -66, -64, -62, -54, -52, -52, -46, -42, -22, -20, -14, -10, -4, 8, 14, 22, 64, 74, 78, 88, 96, 96], [-98, -82, -78, -58, -54, -54, -52, -52, -46, -46, -40, -40, -28, -26, -4, 0, 8, 8, 12, 14, 50, 52, 62, 66, 68, 70, 78, 94, 96], [-94, -90, -80, -78, -74, -72, -70, -54, -52, -46, -40, -38, -28, -22, -22, -20, 16, 16, 18, 18, 20, 24, 44, 46, 50, 58, 64, 70, 76], [-96, -94, -92, -86, -80, -80, -76, -76, -72, -68, -52, -32, -26, -18, -14, -10, -2, 0, 4, 10, 12, 18, 22, 30, 44, 70, 76, 78, 82], [-90, -88, -68, -66, -46, -40, -40, -30, -30, -26, -22, -18, -6, -4, -4, 6, 8, 10, 10, 16, 20, 20, 26, 28, 36, 58, 82, 90, 98], [-90, -86, -84, -84, -82, -66, -60, -40, -32, -22, -14, 4, 6, 20, 22, 22, 32, 34, 34, 52, 58, 60, 66, 70, 76, 80, 88, 92, 96], [-96, -90, -80, -80, -66, -66, -46, -36, -36, -28, -20, -10, -4, 0, 14, 20, 24, 26, 32, 38, 38, 44, 60, 70, 70, 76, 78, 86, 94], [-94, -82, -80, -72, -70, -60, -46, -46, -38, -36, -26, -24, -18, -12, -4, 18, 26, 34, 38, 44, 46, 50, 52, 64, 68, 72, 80, 80, 96], [-98, -94, -92, -84, -76, -66, -62, -44, -36, -34, -32, -22, 2, 4, 8, 18, 18, 18, 18, 32, 36, 42, 52, 58, 70, 80, 86, 94, 98], [-98, -96, -92, -82, -74, -72, -72, -28, -2, 0, 4, 20, 32, 32, 34, 34, 36, 38, 50, 52, 58, 60, 62, 62, 80, 84, 88, 88, 90], [-74, -74, -70, -66, -54, -50, -42, -40, -36, -16, -14, -14, -12, -10, -8, -4, 10, 18, 28, 58, 60, 68, 68, 74, 76, 84, 86, 96, 98], [-98, -96, -90, -56, -54, -46, -42, -36, -34, -26, -26, -6, 0, 2, 12, 14, 24, 24, 40, 50, 60, 64, 64, 70, 76, 78, 80, 88, 90], [-92, -92, -84, -80, -80, -64, -56, -50, -44, -42, -32, -18, -16, -14, 14, 24, 26, 26, 30, 36, 44, 46, 46, 50, 56, 64, 86, 86, 86], [-96, -94, -94, -88, -86, -74, -62, -62, -44, -40, -30, -28, -24, -20, 14, 20, 22, 40, 52, 52, 56, 58, 60, 60, 62, 62, 84, 96, 98], [-98, -92, -92, -54, -54, -50, -48, -48, -40, -40, -30, -26, -24, -12, -6, 0, 18, 24, 24, 26, 26, 36, 44, 48, 66, 74, 86, 88, 94], [-98, -98, -94, -90, -88, -80, -76, -68, -60, -58, -56, -42, -38, -28, -26, -4, 0, 20, 22, 28, 36, 50, 56, 56, 60, 60, 68, 86, 86], [-94, -84, -62, -42, -36, -36, -28, -26, -24, -20, -14, -10, 0, 16, 20, 22, 30, 34, 40, 52, 56, 56, 62, 66, 76, 82, 84, 92, 98], [-98, -92, -86, -86, -78, -76, -58, -58, -54, -50, -40, -26, -10, -6, 0, 18, 20, 24, 24, 24, 38, 42, 46, 54, 64, 76, 80, 90, 96], [-86, -84, -78, -76, -66, -62, -60, -56, -46, -32, -22, -18, -18, -10, -2, 4, 10, 14, 28, 36, 42, 42, 56, 60, 62, 68, 74, 82, 88], [-98, -98, -76, -72, -64, -64, -62, -60, -48, -44, -42, -36, -36, -30, -24, -12, -8, 2, 12, 16, 36, 42, 44, 60, 66, 68, 84, 86, 88], [-96, -96, -94, -94, -92, -90, -62, -50, -48, -48, -48, -44, -24, -22, -8, -8, -6, -6, 0, 16, 48, 54, 54, 58, 64, 74, 74, 78, 88], [-98, -96, -84, -74, -54, -52, -40, -34, -24, -16, -14, -10, -6, -6, -4, 12, 16, 18, 46, 46, 48, 48, 56, 62, 64, 78, 82, 86, 90], [-86, -86, -72, -66, -62, -48, -44, -38, -26, -22, -20, -12, -4, 8, 10, 14, 18, 30, 30, 32, 42, 62, 66, 70, 70, 78, 84, 94, 98], [-98, -88, -82, -80, -68, -68, -68, -66, -64, -52, -50, -46, -44, -42, -36, -34, -2, -2, 4, 10, 26, 42, 44, 62, 66, 68, 76, 82, 98], [-98, -92, -88, -88, -86, -62, -50, -46, -32, -28, -20, -4, -2, 0, 12, 20, 34, 38, 42, 60, 64, 64, 64, 66, 66, 72, 74, 88, 98]],16,),
    ([[1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0], [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0], [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0], [1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0], [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0]],35,),
    ([[12, 22, 56, 63, 69], [8, 8, 12, 57, 95], [40, 55, 59, 65, 72], [2, 22, 40, 72, 83], [2, 4, 12, 31, 38]],4,),
    ([[-92, -36, 84, 62, -94, -74, 20, 20, 92], [52, -40, -98, -32, 58, 80, -60, 46, 80], [8, 8, 0, -48, -86, 48, -38, -96, 92], [18, -68, -74, 92, -70, -36, -32, -16, -16], [-70, -26, 32, -58, 82, 22, -12, 96, -44], [-68, -54, -94, -84, -68, -70, -30, -76, -52], [-68, 64, 68, 80, 30, 12, -82, 20, -58], [-38, -88, 24, 28, -98, 56, -62, -46, 98], [28, -82, -32, 74, -94, 38, -12, -46, -6]],4,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],35,),
    ([[78, 96, 83, 94, 61, 52, 86, 42, 64, 39, 8, 48, 87, 31, 77, 72, 9, 9, 3, 83, 2, 79, 20, 84, 50, 85, 32, 15, 14, 70, 7, 19, 43, 6, 71, 16], [35, 5, 20, 49, 27, 85, 22, 1, 99, 13, 57, 86, 70, 34, 34, 11, 50, 22, 60, 58, 31, 45, 64, 3, 74, 95, 85, 46, 32, 94, 13, 90, 94, 56, 25, 94], [52, 7, 25, 18, 38, 42, 26, 83, 41, 20, 38, 29, 71, 38, 99, 53, 76, 61, 98, 56, 74, 46, 62, 1, 1, 98, 7, 36, 87, 66, 77, 52, 81, 27, 44, 54], [12, 17, 86, 71, 29, 39, 95, 71, 53, 32, 65, 93, 66, 62, 97, 63, 99, 48, 33, 7, 28, 20, 68, 98, 45, 92, 9, 94, 29, 43, 24, 99, 9, 99, 39, 88], [25, 71, 58, 33, 26, 76, 27, 56, 55, 60, 28, 36, 10, 18, 71, 98, 61, 83, 18, 62, 43, 57, 23, 61, 43, 34, 66, 76, 25, 82, 73, 79, 76, 13, 6, 31], [79, 36, 81, 72, 22, 53, 90, 82, 99, 10, 42, 11, 36, 80, 30, 95, 90, 71, 57, 62, 38, 97, 73, 47, 66, 15, 59, 62, 26, 7, 25, 93, 35, 24, 4, 19], [49, 55, 96, 83, 54, 53, 41, 35, 52, 83, 46, 58, 50, 48, 53, 41, 69, 36, 93, 27, 7, 42, 95, 90, 7, 29, 93, 23, 43, 18, 78, 13, 70, 18, 19, 91], [74, 42, 96, 90, 95, 25, 48, 8, 19, 48, 59, 79, 64, 90, 67, 76, 33, 60, 25, 32, 92, 12, 38, 12, 52, 73, 84, 62, 72, 82, 76, 30, 95, 15, 22, 30], [61, 90, 92, 47, 62, 34, 56, 90, 12, 81, 48, 3, 37, 43, 78, 41, 42, 78, 22, 35, 36, 98, 77, 70, 22, 32, 88, 22, 66, 64, 81, 88, 63, 67, 48, 51], [39, 21, 32, 61, 54, 32, 98, 87, 66, 71, 31, 81, 68, 3, 60, 67, 1, 71, 24, 64, 52, 99, 25, 85, 60, 3, 17, 93, 61, 74, 44, 27, 74, 42, 70, 22], [98, 61, 8, 13, 47, 31, 11, 99, 47, 3, 21, 28, 67, 3, 35, 67, 71, 32, 85, 62, 6, 94, 99, 41, 34, 7, 81, 22, 74, 15, 78, 48, 86, 38, 54, 21], [57, 49, 87, 34, 93, 5, 91, 89, 46, 63, 13, 89, 59, 56, 67, 24, 12, 57, 96, 66, 44, 32, 90, 23, 14, 10, 28, 12, 66, 74, 17, 4, 82, 92, 27, 62], [3, 62, 20, 85, 22, 98, 38, 68, 57, 37, 98, 22, 82, 34, 65, 99, 61, 66, 8, 36, 92, 50, 12, 73, 64, 4, 61, 31, 25, 2, 59, 68, 47, 28, 86, 93], [28, 6, 38, 36, 93, 72, 39, 55, 30, 76, 96, 54, 5, 73, 15, 14, 12, 74, 65, 44, 94, 91, 6, 33, 42, 87, 35, 81, 57, 10, 11, 33, 86, 73, 89, 94], [8, 10, 9, 84, 30, 9, 35, 86, 49, 37, 43, 23, 43, 13, 36, 82, 61, 34, 12, 73, 4, 70, 32, 17, 34, 35, 64, 80, 19, 50, 58, 77, 44, 66, 1, 46], [99, 72, 9, 61, 48, 92, 58, 68, 33, 52, 8, 47, 14, 9, 13, 2, 11, 49, 3, 64, 60, 95, 64, 59, 36, 52, 10, 50, 86, 9, 31, 80, 31, 91, 9, 25], [74, 65, 81, 28, 88, 58, 49, 92, 17, 14, 31, 27, 61, 52, 15, 40, 33, 38, 28, 92, 71, 56, 34, 49, 2, 55, 33, 3, 3, 61, 66, 95, 79, 62, 79, 91], [47, 87, 29, 43, 72, 14, 76, 93, 41, 18, 65, 2, 17, 20, 48, 59, 97, 43, 94, 59, 61, 79, 71, 54, 93, 8, 86, 4, 73, 10, 66, 98, 29, 48, 11, 72], [32, 79, 33, 43, 27, 60, 73, 55, 27, 84, 4, 97, 39, 5, 25, 23, 98, 1, 7, 4, 48, 47, 34, 79, 17, 89, 87, 8, 37, 22, 80, 21, 81, 74, 73, 31], [97, 59, 19, 17, 65, 65, 21, 37, 30, 76, 41, 86, 84, 30, 33, 32, 38, 7, 30, 56, 19, 80, 86, 62, 47, 19, 45, 80, 16, 82, 44, 27, 7, 38, 6, 30], [64, 83, 75, 9, 41, 8, 61, 89, 61, 49, 40, 67, 75, 27, 80, 9, 30, 12, 99, 20, 93, 42, 99, 88, 76, 1, 56, 10, 34, 41, 50, 97, 66, 62, 52, 49], [64, 54, 22, 65, 92, 84, 27, 42, 10, 69, 67, 18, 75, 24, 38, 71, 52, 79, 18, 38, 70, 94, 91, 77, 38, 74, 91, 3, 1, 85, 82, 1, 52, 40, 44, 60], [83, 17, 61, 43, 30, 62, 60, 35, 39, 95, 91, 71, 2, 50, 7, 32, 51, 44, 24, 18, 66, 87, 62, 3, 92, 87, 77, 1, 25, 46, 77, 15, 59, 46, 88, 86], [83, 66, 34, 2, 59, 29, 65, 98, 55, 93, 66, 26, 75, 36, 64, 60, 45, 19, 75, 40, 16, 34, 52, 25, 8, 52, 29, 39, 92, 17, 70, 29, 42, 33, 23, 80], [22, 11, 32, 56, 48, 20, 32, 33, 49, 59, 13, 53, 79, 4, 33, 11, 6, 71, 86, 14, 98, 61, 20, 80, 2, 53, 68, 9, 50, 26, 73, 20, 87, 60, 96, 99], [96, 64, 95, 64, 34, 73, 24, 52, 46, 28, 94, 82, 26, 1, 74, 47, 14, 48, 5, 33, 65, 84, 72, 21, 10, 60, 69, 65, 57, 16, 73, 2, 28, 42, 14, 44], [57, 72, 10, 97, 89, 71, 74, 20, 5, 82, 52, 86, 39, 67, 93, 19, 81, 53, 21, 72, 64, 6, 61, 47, 89, 54, 72, 47, 18, 97, 53, 48, 75, 65, 99, 33], [61, 22, 43, 17, 71, 62, 73, 94, 48, 51, 85, 46, 41, 66, 31, 43, 7, 29, 3, 61, 28, 62, 56, 34, 61, 59, 49, 38, 14, 33, 64, 94, 14, 27, 42, 28], [93, 66, 93, 79, 99, 47, 2, 8, 26, 82, 73, 3, 5, 43, 80, 74, 29, 94, 11, 16, 31, 89, 16, 74, 95, 87, 43, 15, 77, 80, 57, 27, 92, 74, 6, 69], [64, 88, 68, 15, 45, 85, 22, 39, 62, 24, 92, 7, 61, 69, 51, 32, 81, 81, 62, 68, 39, 26, 38, 97, 62, 70, 84, 80, 42, 3, 60, 89, 2, 61, 39, 90], [29, 39, 6, 62, 21, 87, 37, 64, 88, 68, 5, 75, 96, 72, 37, 39, 23, 97, 58, 57, 81, 74, 72, 91, 58, 52, 68, 47, 64, 46, 60, 60, 65, 31, 65, 46], [81, 39, 17, 69, 41, 21, 62, 88, 29, 31, 3, 73, 28, 99, 30, 39, 48, 28, 52, 62, 57, 5, 9, 5, 24, 77, 22, 2, 44, 74, 59, 68, 37, 65, 94, 34], [47, 49, 70, 54, 77, 78, 41, 1, 63, 45, 9, 34, 18, 74, 57, 70, 75, 86, 67, 5, 35, 92, 10, 40, 59, 83, 29, 16, 37, 16, 80, 4, 95, 26, 23, 17], [80, 56, 23, 61, 92, 5, 29, 39, 82, 8, 30, 80, 66, 62, 31, 20, 63, 75, 65, 80, 63, 89, 14, 22, 45, 81, 9, 97, 99, 5, 41, 96, 24, 90, 98, 67], [50, 69, 72, 14, 34, 42, 75, 83, 23, 33, 14, 49, 59, 98, 29, 44, 87, 18, 79, 26, 32, 33, 63, 53, 37, 1, 71, 66, 12, 30, 46, 69, 6, 45, 45, 18], [21, 55, 93, 44, 14, 50, 63, 41, 47, 23, 15, 25, 63, 19, 31, 63, 76, 32, 79, 18, 47, 93, 98, 43, 79, 60, 43, 8, 15, 94, 56, 34, 41, 74, 75, 15]],29,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))