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


func f_gold(n int, m int) int {
	if n == m {
		return n
	}
	return 1
}
//TOFILL
func main() {
	var (
		n_success int     = 0
		param0    []int = []int{57, 22, 17, 74, 93, 56, 5, 5, 9, 98}
		param1    []int = []int{57, 22, 17, 74, 22, 54, 33, 68, 75, 21}
	)
	for i := int(0); i < len(param0[:]); i++ {
		if f_filled(param0[i], param1[i]) == f_gold(param0[i], param1[i]) {
			n_success += 1
		}
	}
	fmt.Print("#Results:", " ", n_success, ", ", len(param0[:]))
	os.Exit(0)
}
