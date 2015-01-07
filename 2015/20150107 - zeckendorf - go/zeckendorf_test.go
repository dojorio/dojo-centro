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
		{5, 1000},
	} {
		if value := zeckendorf(tc.in); value != tc.out {
			t.Errorf("Errado zeckendorf(%v) -> %v != %v", tc.in, value, tc.out)
		}
	}
}
