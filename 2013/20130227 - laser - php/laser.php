<?php

class Inimigo {
	function __construct($x, $y){
		$this->x = $x;
		$this->y = $y;
	}
}

function laser($inimigos) {
	if (isset($inimigos[1]) and (
			$inimigos[1]->x == $inimigos[0]->x or 
			$inimigos[1]->y == $inimigos[0]->y)) {
		return 1;
	}
		

	if (isset($inimigos[2])) {
		return 2;
	}

	return count($inimigos);
}