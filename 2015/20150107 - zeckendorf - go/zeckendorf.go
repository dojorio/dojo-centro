package zeckendorf

import "math"

func zeckendorf(number int) int {
	fibo := []int{1, 2}

	for fibo[len(fibo)-1] < number {
		fibo = append(fibo, fibo[len(fibo)-1]+fibo[len(fibo)-2])
	}

	r := 0

	for c := len(fibo) - 1; c > -1; c-- {
		if fibo[c] <= number {
			r += int(math.Pow10(c))
			number -= fibo[c]
		}
	}

	return r
}
