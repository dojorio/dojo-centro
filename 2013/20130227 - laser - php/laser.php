<?php

class Inimigo {
	function __construct($x, $y){
		$this->x = $x;
		$this->y = $y;
	}
}

function laser($inimigos) {
	$linhas = array();
	$colunas = array();

	if (empty($inimigos))
		return 0;

	foreach ($inimigos as $inimigo) {

		if(isset($linhas[$inimigo->x])){
			$linhas[$inimigo->x]++;
		}else{
			$linhas[$inimigo->x] = 1;
		}

		if(isset($colunas[$inimigo->y])){
			$colunas[$inimigo->y]++;
		}else{
			$colunas[$inimigo->y] = 1;
		}

	}

	$maiorLinha = max($linhas);
	$maiorColuna = max($colunas);

	
	if($maiorLinha > $maiorColuna) {
		$maiorLinha = array_search($maiorLinha, $linhas);

		foreach ($inimigos as $key => $inimigo) {
			if ($inimigo->x == $maiorLinha) {
				unset($inimigos[$key]);
			}
		}
	} else {
		$maiorColuna = array_search($maiorColuna, $colunas);

		foreach ($inimigos as $key => $inimigo) {
			if ($inimigo->y == $maiorColuna) {
				unset($inimigos[$key]);
			}
		}
	}

	return 1 + laser($inimigos);
}


