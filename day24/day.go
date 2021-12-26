package main

import (
	"fmt"
)

func equ(a, b int) int {
	if a == b {
		return 1
	}
	return 0
}

func func00(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 1
	x += 15
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 4
	y *= x
	z += y
	return z
}

func func01(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 1
	x += 14
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 16
	y *= x
	z += y
	return z
}

func func02(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 1
	x += 11
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 14
	y *= x
	z += y
	return z
}

func func03(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 26
	x += -13
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 3
	y *= x
	z += y
	return z
}

func func04(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 1
	x += 14
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 11
	y *= x
	z += y
	return z
}

func func05(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 1
	x += 15
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 13
	y *= x
	z += y
	return z
}

func func06(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 26
	x += -7
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 11
	y *= x
	z += y
	return z
}

func func07(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 1
	x += 10
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 7
	y *= x
	z += y
	return z
}

func func08(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 26
	x += -12
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 12
	y *= x
	z += y
	return z
}

func func09(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 1
	x += 15
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 15
	y *= x
	z += y
	return z
}

func func10(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 26
	x += -16
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 13
	y *= x
	z += y
	return z
}

func func11(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 26
	x += -9
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 1
	y *= x
	z += y
	return z
}

func func12(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 26
	x += -8
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 15
	y *= x
	z += y
	return z
}

func func13(w, z int) int {
	var x, y int
	x *= 0
	x += z
	x %= 26
	z /= 26
	x += -8
	x = equ(x, w)
	x = equ(x, 0)
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 4
	y *= x
	z += y
	return z
}

const maxZ = 1e6

func part1() [14]int {

	var (
		ws     [14]int
		search func(int, int) bool
	)

	funcs := [14]func(int, int) int{func00, func01, func02, func03, func04,
		func05, func06, func07, func08, func09, func10, func11, func12, func13}

	search = func(z_out, i int) bool {
		fmt.Printf("i: %#v\n", i)
		for w := 9; w > 0; w-- {
			ws[i] = w
			for z_in := 0; z_in < maxZ; z_in++ {
				if funcs[i](w, z_in) == z_out {
					if i == 0 {
						return true
					}
					if search(z_in, i-1) {
						return true
					}
				}
			}
		}
		return false
	}

	search(0, 13)
	return ws
}

func main() {
	fmt.Println(part1())
}
