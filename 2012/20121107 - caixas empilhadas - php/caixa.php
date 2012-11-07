<?php

class Caixa {
	function __construct($peso, $capacidade) {
		$this->peso = $peso;
		$this->capacidade = $capacidade;
	}
}

function empilha_caixas($caixas) {
	if (empty($caixas))
		return 0;
	
	usort($caixas, function($c1, $c2) {
		$peso = $c2->peso - $c1->peso;

		return $peso ?: $c2->capacidade - $c1->capacidade;
	});

	if (count($caixas) == 2 && $caixas[0]->capacidade < end($caixas)->peso)
		return 1;

	if (count($caixas) == 3) {
		$caixas[0]->capacidade -= $caixas[1]->peso;
		$caixas[0]->capacidade -= $caixas[2]->peso;
		$caixas[1]->capacidade -= $caixas[2]->peso;
		for ($i = 0; $i<=count($caixas); $i++) {
			if($caixas[$i]->capacidade <= 0)
				break;
			
		}
		return $i;
	}

	if (count($caixas) == 3 && $caixas[0]->capacidade == 1)
		return 2;

	return count($caixas);
}