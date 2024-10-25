package main

import (
			"fmt"
"sort"
	"math"
	"os"
	"unsafe"
)

func min(x int, y int) int {
	if x < y {
		return x
	}
	return y
}
func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}
func cmpfunc(a unsafe.Pointer, b unsafe.Pointer) int {
	return *(*int)(a) - *(*int)(b)
}


func f_gold(A []int, B []int, m int, n int) int {
	sort.Ints(A)
	sort.Ints(B)
	var a int = 0
	var b int = 0
	var result int = math.MaxInt64
	for a < m && b < n {
		if math.Abs(float64(A[a]-B[b])) < float64(result) {
			result = int(math.Abs(float64(A[a] - B[b])))
		}
		if A[a] < B[b] {
			a++
		} else {
			b++
		}
	}
	return result
}
//TOFILL
func main() {
	var (
		n_success int      = 0
		param0_0  []int  = []int{2, 2, 11, 13, 18, 18, 23, 25, 28, 28, 37, 39, 53, 56, 67, 70, 74, 74, 75, 79, 80, 82, 84, 89, 94, 95, 95, 98, 98}
		param0_1  []int  = []int{-78, 10, -8, 30, -70, -94, -48, -4, -22, -40, -36, -48, -4, 86, -50, 62, -72, -44, -62, 22, -30, -72, 6, -24, -78, 72, -44, 56, 38, -36, 0, -72, -10, -12, -70, -64, -24}
		param0_2  []int  = []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
		param0_3  []int  = []int{57, 82, 90, 9, 61, 71, 15, 2, 39, 24, 28, 28, 47}
		param0_4  []int  = []int{-92, -90, -90, -28, -16, -14, -14, -8, 42, 52, 62, 84}
		param0_5  []int  = []int{1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0}
		param0_6  []int  = []int{6, 7, 7, 12, 15, 15, 21, 24, 26, 26, 28, 36, 38, 42, 46, 52, 55, 56, 59, 62, 63, 65, 65, 66, 68, 71, 73, 77, 77, 77, 77, 85, 87, 87, 88, 90, 93, 94, 98}
		param0_7  []int  = []int{-68, 44, 88, -68, 22, 34, -82, 18, -60, 30, 24, 18, 78, 90, -20, -60, 94, 70, 4, -16, -38}
		param0_8  []int   = []int{0, 0, 1}
		param0_9  []int  = []int{14, 7, 9, 71, 37, 20, 85, 62, 70, 67, 26, 47, 61, 99, 2, 90, 70, 46, 53, 16, 56, 7, 15, 81, 85, 94, 73, 40, 35, 58, 21, 98, 45}
		param0    [][]int = [][]int{param0_0, param0_1, param0_2, param0_3, param0_4, param0_5, param0_6, param0_7, param0_8, param0_9}
		param1_0  []int  = []int{5, 6, 11, 13, 13, 16, 17, 19, 23, 25, 28, 31, 31, 39, 41, 44, 45, 52, 62, 64, 70, 71, 73, 78, 78, 79, 85, 86, 92}
		param1_1  []int  = []int{78, -80, -24, -50, -26, -62, 26, -12, 22, -90, 84, 10, 18, 62, 26, -68, 92, 64, -52, 76, -84, 64, 50, 36, -24, -98, 42, 72, -78, -98, -24, 86, 2, 60, -30, 14, -42}
		param1_2  []int  = []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
		param1_3  []int  = []int{85, 92, 84, 27, 54, 77, 26, 49, 47, 51, 70, 11, 41}
		param1_4  []int  = []int{-98, -98, -58, -6, 14, 16, 18, 46, 52, 52, 52, 56}
		param1_5  []int  = []int{0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1}
		param1_6  []int  = []int{1, 3, 4, 4, 6, 7, 8, 8, 15, 17, 18, 18, 20, 23, 23, 24, 25, 25, 26, 33, 39, 43, 46, 54, 59, 67, 69, 69, 69, 69, 76, 76, 81, 81, 85, 86, 86, 91, 95}
		param1_7  []int  = []int{-18, -30, -74, -50, 98, -44, -62, -20, 18, 84, 62, -64, -2, 62, -32, -34, -14, -52, -36, -60, -68}
		param1_8  []int   = []int{0, 0, 1}
		param1_9  []int  = []int{99, 72, 29, 55, 88, 1, 88, 19, 7, 80, 79, 18, 28, 41, 48, 49, 67, 27, 24, 94, 86, 14, 45, 84, 37, 71, 92, 98, 16, 64, 67, 44, 29}
		param1    [][]int = [][]int{param1_0, param1_1, param1_2, param1_3, param1_4, param1_5, param1_6, param1_7, param1_8, param1_9}
		param2    []int  = []int{28, 23, 14, 7, 11, 35, 30, 16, 2, 20}
		param3    []int  = []int{14, 33, 16, 8, 6, 33, 20, 12, 1, 25}
	)
	for i := int(0); i < len(param0[:]); i++ {
		if f_filled(([]int)(param0[i]), ([]int)(param1[i]), param2[i], param3[i]) == f_gold(([]int)(param0[i]), ([]int)(param1[i]), param2[i], param3[i]) {
			n_success += 1
		}
	}
	fmt.Print("#Results:", " ", n_success, ", ", len(param0[:]))
	os.Exit(0)
}
