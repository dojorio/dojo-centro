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

	$linhas = array();
	$colunas = array();

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

	
	if (($maiorLinha > $maiorColuna) && count($linhas) < count($colunas)) {
		$maiorLinha = array_search($maiorLinha, $linhas);
		$maiorColuna = false;
	} else if (count($linhas) > count($colunas)){
		$maiorColuna = array_search($maiorColuna, $colunas);
		$maiorLinha = false;	
	}else{
		$maiorLinha = array_search($maiorLinha, $linhas);
		$maiorColuna = false;
	}

	foreach ($inimigos as $key => $inimigo) {
		if ($inimigo->x === $maiorLinha or $inimigo->y === $maiorColuna) {
			unset($inimigos[$key]);
		}
	}

	return 1 + laser($inimigos);
}


