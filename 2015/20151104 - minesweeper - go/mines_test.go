package mines

import "testing"

type TestCase struct {
	in, out string
}

func TestMines(t *testing.T) {
	for i, tc := range []TestCase{
		{"*", "*"},
		{".", "0"},
		{"..", "00"},
		{"**", "**"},
		{"*.", "*1"},
		{".*", "1*"},
	} {
		if value := FillMines(tc.in); value != tc.out {
			t.Errorf("test %d: FillMines(%q) = %q; want %q", i, tc.in, value, tc.out)
		}
	}
}
