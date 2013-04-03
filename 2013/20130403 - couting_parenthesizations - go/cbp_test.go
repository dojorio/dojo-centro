package main

import "testing"

// http://people.csail.mit.edu/bdean/6.046/dp/
// Counting Boolean Parenthesizations

func TestUmaPossibilidade(t *testing.T) {
	tests := map[string]int {
		"T": 1,
		"F": 0,
		"TvT": 1,
		"TvTvT": 2,
		"TvTvTvT": 5,
	}
	for entrada, esperado := range(tests) {
		resultado := ContagemDePossibilidades(entrada)
		if resultado != esperado {
			t.Errorf("%d diferente de %d", resultado, esperado)
		}
	}
}
