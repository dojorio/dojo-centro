package main

import "testing"

// http://people.csail.mit.edu/bdean/6.046/dp/
// Counting Boolean Parenthesizations

func TestUmaPossibilidade(t *testing.T) {
	tests := map[string]int {
		"F": 0,
		"T": 1,
		"TvT": 1,
		"TvTvT": 2,
		"TvTvTvT": 5,
		"TvTvTvTvT": 14,
		"TvTvTvTvF": 14,
		// T v TvTvTvT 1*5
		// TvT v TvTvT 1*2
		// TvTvT v TvT 2*1
		// TvTvTvT v F 5*1
	}

	for entrada, esperado := range(tests) {
		resultado := ContagemDePossibilidades(entrada)
		if resultado != esperado {
			t.Errorf("%d diferente de %d", resultado, esperado)
		}
	}
}
