package mines

import "testing"

func TestMines(t *testing.T) {
	// "*" -> "*"
	got := FillMines("*")
	want := "*"

	if got != want {
		t.Errorf("FillMines() = %v; want %v", got, want)
	}


	// "." -> "0"
	got = FillMines(".")
	want = "0"

	if got != want {
		t.Errorf("FillMines() = %v; want %v", got, want)
	}


	// ".." -> "00"
	got = FillMines("..")
	want = "00"

	if got != want {
		t.Errorf("FillMines() = %v; want %v", got, want)
	}

	// "**" -> "**"
	got = FillMines("**")
	want = "**"

	if got != want {
		t.Errorf("FillMines() = %v; want %v", got, want)
	}
}