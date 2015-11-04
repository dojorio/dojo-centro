package mines

import "testing"

func TestMines(t *testing.T) {
	// "*" -> "*"
	got := FillMines("*")
	want := "*"
	if got != want {
		t.Errorf("FillMines() = %v; want %v", got, want)
	}
}