package zeckendorf

import "math"

func zeckendorf(number int) int {
	fibo := []int{1, 2, 3, 5, 8, 13, 21}

	c := len(fibo) - 1
	r := 0

	for i := range fibo {
		if fibo[c-i] <= number {
			r += int(math.Pow10(c - i))
			number -= fibo[c-i]
		}
	}

	return r
}
