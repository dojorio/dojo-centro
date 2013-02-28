<?php

class Inimigo {
	function __construct($x, $y){
		$this->x = $x;
		$this->y = $y;
	}
}

function laser($inimigos) {
	if (empty($inimigos))
		return 0;

	$linhas = $colunas = array();

	foreach ($inimigos as $inimigo) {
		if (!isset($linhas[$inimigo->x]))
			$linhas[$inimigo->x] = 0;

		if (!isset($colunas[$inimigo->y]))
			$colunas[$inimigo->y] = 0;

		$linhas[$inimigo->x]++;
		$colunas[$inimigo->y]++;
	}
	
	// Escolhe qual linha ou coluna atirar
	if (count($linhas) < count($colunas)) {
		$maiorLinha = array_search(max($linhas), $linhas);
		$maiorColuna = false;
	} else {
		$maiorColuna = array_search(max($colunas), $colunas);
		$maiorLinha = false;	
	}

	// Remove os inimigos da linha/coluna escolhida
	foreach ($inimigos as $key => $inimigo) {
		if ($inimigo->x === $maiorLinha or $inimigo->y === $maiorColuna) {
			unset($inimigos[$key]);
		}
	}

	return 1 + laser($inimigos);
}


