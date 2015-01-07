package zeckendorf

import "math"

func zeckendorf(number int) int {
	fibo := []int{1, 2, 3, 5, 8}

	for i, n := range fibo {
		if n == number {
			return int(math.Pow10(i))
		}
	}

	return -1
}
