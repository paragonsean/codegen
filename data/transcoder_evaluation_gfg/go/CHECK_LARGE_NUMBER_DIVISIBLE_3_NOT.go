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


func f_gold(str []byte) int {
	var (
		n        int = int(len(str))
		digitSum int = 0
	)
	for i := int(0); i < n; i++ {
		digitSum += int(str[i] - byte('0'))
	}
	return digitSum%3
}
//TOFILL
func main() {
	var (
		n_success int           = 0
		param0    [10][]byte = [10][]byte{func() []byte {
			var t []byte
			copy(t[:], ([]byte)("Xy"))
			return t
		}(), func() []byte {
			var t []byte
			copy(t[:], ([]byte)("4827182"))
			return t
		}(), func() []byte {
			var t []byte
			copy(t[:], ([]byte)("110011"))
			return t
		}(), func() []byte {
			var t []byte
			copy(t[:], ([]byte)("GdOXZk"))
			return t
		}(), func() []byte {
			var t []byte
			copy(t[:], ([]byte)("8970294"))
			return t
		}(), func() []byte {
			var t []byte
			copy(t[:], ([]byte)("000110"))
			return t
		}(), func() []byte {
			var t []byte
			copy(t[:], ([]byte)("xMRGdAgsGlH"))
			return t
		}(), func() []byte {
			var t []byte
			copy(t[:], ([]byte)("34643260819239"))
			return t
		}(), func() []byte {
			var t []byte
			copy(t[:], ([]byte)("00"))
			return t
		}(), func() []byte {
			var t []byte
			copy(t[:], ([]byte)("DcCK"))
			return t
		}()}
	)
	for i := int(0); i < len(param0[:]); i++ {
		if f_filled(param0[i][:]) == f_gold(param0[i][:]) {
			n_success += 1
		}
	}
	fmt.Print("#Results:", " ", n_success, ", ", len(param0[:]))
	os.Exit(0)
}
