package zeckendorf

import "testing"

type TestCase struct {
	in, out int
}

func Test_1(t *testing.T) {
	for _, tc := range []TestCase{
		{1, 1},
		{2, 10},
		{3, 100},
	} {
		if zeckendorf(tc.in) != tc.out {
			t.Errorf("Errado zeckendorf(%v) != %v", tc.in, tc.out)
		}
	}
}
