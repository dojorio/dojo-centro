<?php

class Inimigo {
	public $x;
	public $y;
	
	function __constructor($x, $y){
		$this->x = $x;
		$this->y = $y;
	}
}

function laser($inimigos) {
	if (isset($inimigos[1]) and (
			$inimigos[1]->x == $inimigos[0]->x or 
			$inimigos[1]->y == $inimigos[0]->y ))
		return 1;
	return count($inimigos);
}