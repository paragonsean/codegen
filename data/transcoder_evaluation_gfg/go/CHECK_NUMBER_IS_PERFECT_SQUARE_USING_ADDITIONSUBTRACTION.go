package main

import (
		"fmt"
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


func f_gold(n int) bool {
	for sum, i := int(0), int(1); sum < n; i += 2 {
		sum += i
		if sum == n {
			return true
		}
	}
	return false
}
//TOFILL
func main() {
	var (
		n_success int     = 0
		param0    []int = []int{1, 4, 9, 25, 36, 3, 121, 14, 17, 80}
	)
	for i := int(0); i < len(param0[:]); i++ {
		if f_filled(param0[i]) == f_gold(param0[i]) {
			n_success += 1
		}
	}
	fmt.Print("#Results:", " ", n_success, ", ", len(param0[:]))
	os.Exit(0)
}
