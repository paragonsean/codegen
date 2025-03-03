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


func f_gold(n int) int {
	var sum int = 0
	for i := int(0); i < n; i++ {
		sum += i * (n - i)
	}
	return sum * 2
}
//TOFILL
func main() {
	var (
		n_success int     = 0
		param0    []int = []int{63, 72, 28, 35, 6, 70, 20, 8, 8, 35}
	)
	for i := int(0); i < len(param0[:]); i++ {
		if f_filled(param0[i]) == f_gold(param0[i]) {
			n_success += 1
		}
	}
	fmt.Print("#Results:", " ", n_success, ", ", len(param0[:]))
	os.Exit(0)
}
