package main

import "testing"

func Test001(t *testing.T) {
	resultado := cbp("T")
	if resultado != 1{
		t.Errorf("%d diferente de %d", 2, 3)
	}
}
