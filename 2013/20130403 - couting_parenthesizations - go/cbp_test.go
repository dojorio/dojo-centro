package main

import "testing"


func TestUmaPossibilidade(t *testing.T) {
	resultado := contagem_de_possibilidades("T")
	esperado := 1
	if resultado != esperado {
		t.Errorf("%d diferente de %d", resultado, esperado)
	}
}

func TestNenhumaPossibilidade(t *testing.T) {
	resultado := contagem_de_possibilidades("F")
	esperado := 0
	if resultado != esperado {
		t.Errorf("%d diferente de %d", resultado, esperado)
	}
}

func TestVerdadeiroOuVerdadeiro(t *testing.T) {
	resultado := contagem_de_possibilidades("TvT")
	esperado := 1
	if resultado != esperado {
		t.Errorf("%d diferente de %d", resultado, esperado)
	}
}
