package mines

import "testing"

type TestCase struct {
	in  Board
	out string
}

func TestMines(t *testing.T) {
	_ = Board([][]rune{{'*'}})
	for i, tc := range []TestCase{
		TestCase{Board{{'*'}}, "*"},
		// {{'.'}, "0"},
		// {{'.', '.'}, "00"},
		// {{'*', '*'}, "**"},
		// {{'*', '.'}, "*1"},
		// {{'.', '*'}, "1*"},
		// {{'*', '.', '*'}, "*2*"},
		// {{'*', '*', '.'}, "**1"},
		// {{'*', '.', '.'}, "*10"},
		// {{'*', '.', '*', '.'}, "*2*1"},
		// {{'*', '.', '*', '.', '.'}, "*2*10"},
	} {
		if value := tc.in.FillMines(); value != tc.out {
			t.Errorf("test %d: FillMines(%q) = %q; want %q", i, tc.in, value, tc.out)
		}
	}
}
