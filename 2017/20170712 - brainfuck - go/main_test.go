package main

import "testing"

func TestInterpretaEspacoVazio(t *testing.T) {
	if "" != Interpreta("") {
		t.Fail()
	}
}