package zeckendorf

import "testing"

func Test_1(t *testing.T) {
	if(zeckendorf(1) != 1) {
		t.Error("Errado zeckendorf(1)")
	}

	if(zeckendorf(2) != 10) {
		t.Error("Errado zeckendorf(2)")
	}
}
