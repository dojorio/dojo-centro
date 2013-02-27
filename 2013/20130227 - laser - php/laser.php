<?php

class Inimigo {
	function __construct($x, $y){
		$this->x = $x;
		$this->y = $y;
	}
}

function laser($inimigos) {
	$linhas = array();
	foreach ($inimigos as $inimigo) {
		$linhas[$inimigo->x] = 'banana';
		$colunas[$inimigo->y] = 'maça';
	}
	return min(count($linhas), count($colunas));
	if (isset($inimigos[1]) and (
			$inimigos[1]->x == $inimigos[0]->x or 
			$inimigos[1]->y == $inimigos[0]->y)) {
		return 1;
	}

	if (isset($inimigos[2]) and (
			$inimigos[2]->x == $inimigos[0]->x or 
			$inimigos[2]->y == $inimigos[0]->y or 
			$inimigos[2]->x == $inimigos[1]->x or 
			$inimigos[2]->y == $inimigos[1]->y)) {
		return 2;
	}

	return count($inimigos);
}