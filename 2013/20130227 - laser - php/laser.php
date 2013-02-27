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
	
	if(max($linhas) > max($colunas)){
		$linha = array_search(max($linhas), $linhas)
		
		laser($linha)
	}

}


