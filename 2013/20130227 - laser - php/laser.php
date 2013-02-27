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
	foreach ($inimigos as $inimigo) {
		$linhas[$inimigo->x] = true;
		$colunas[$inimigo->y] = true;
	}
	return min(count($linhas), count($colunas));
}