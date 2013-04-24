<?php

function ritmo($durações) {
	if (count($durações) == 1) {
		$tempos = count($durações);
		$unidade = $durações[0];
		return "{$tempos}/{$unidade}";
	}

	//if ($durações == array(1, 2, 1))
	//	return '5/2';

	$unidade = max($durações);
	$tempos = array_sum($durações);

	foreach($durações AS &$duração){
		$duração = 1/$duração;
	}
	$soma = array_sum($durações)*2;

	return "{$tempos}/{$unidade}";
}
