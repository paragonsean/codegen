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
	if n <= 1 {
		return false
	}
	for i := int(2); i < n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
//TOFILL
func main() {
	var (
		n_success int     = 0
		param0    []int = []int{37, 39, 73, 8, 28, 66, 20, 36, 6, 51}
	)
	for i := int(0); i < len(param0[:]); i++ {
		if f_filled(param0[i]) == f_gold(param0[i]) {
			n_success += 1
		}
	}
	fmt.Print("#Results:", " ", n_success, ", ", len(param0[:]))
	os.Exit(0)
}
