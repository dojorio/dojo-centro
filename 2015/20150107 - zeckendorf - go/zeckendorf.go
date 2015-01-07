package zeckendorf

import "math"

func zeckendorf(number int) int {
	return 1 * int(math.Pow10(number-1))
}
