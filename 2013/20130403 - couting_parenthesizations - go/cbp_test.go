package main

import "testing"

// http://people.csail.mit.edu/bdean/6.046/dp/
// Counting Boolean Parenthesizations

func TestUmaPossibilidade(t *testing.T) {
	tests := map[string]int {
		"T": 1,
		"F": 0,
	}
	for entrada, esperado := range(tests) {
		resultado := ContagemDePossibilidades(entrada)

	}
	esperado := 1
	if resultado != esperado {
		t.Errorf("%d diferente de %d", resultado, esperado)
	}
}

func TestVerdadeiroOuVerdadeiro(t *testing.T) {
	resultado := ContagemDePossibilidades("TvT")
	esperado := 1
	if resultado != esperado {
		t.Errorf("%d diferente de %d", resultado, esperado)
	}
}

func TestVerdadeiroOuVerdadeiroOuVerdadeiro(t *testing.T) {
	resultado := ContagemDePossibilidades("TvTvT")
	esperado := 2
	if resultado != esperado {
		t.Errorf("%d diferente de %d", resultado, esperado)
	}
}
