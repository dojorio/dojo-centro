package mines

import "testing"

type TestCase struct {
        in, out string
}



func TestMines(t *testing.T) {
	// "*" -> "*"
	got := FillMines("*")
	want := "*"

	if got != want {
		t.Errorf("FillMines() = %v; want %v", got, want)
	}

	for _, tc := range []TestCase{
			{"*", "*"},
	        {".", "0"}, 
	        {"..", "00"},
	        {"**", "**"},
	} {
	        if value := FillMines(tc.in); value != tc.out {
	      		t.Errorf("FillMines() = %v; want %v", value, tc.out)
	        }
	}
}