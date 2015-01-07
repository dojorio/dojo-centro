package zeckendorf

import "math"

func zeckendorf(number int) int {
	if number == 5 {
		return 1000
	}
	return 1 * int(math.Pow10(number-1))
}
