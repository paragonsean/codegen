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


func f_gold(x int) int {
	var m int = 1
	for x&m != 0 {
		x = x ^ m
		m <<= 1
	}
	x = x ^ m
	return x
}
//TOFILL
func main() {
	var (
		n_success int     = 0
		param0    []int = []int{96, 66, 67, 13, 75, 78, 1, 83, 27, 65}
	)
	for i := int(0); i < len(param0[:]); i++ {
		if f_filled(param0[i]) == f_gold(param0[i]) {
			n_success += 1
		}
	}
	fmt.Print("#Results:", " ", n_success, ", ", len(param0[:]))
	os.Exit(0)
}
