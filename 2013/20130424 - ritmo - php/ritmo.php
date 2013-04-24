<?php

function ritmo($durações) {
	if (sizeof(array_unique($durações)) == 2){
		return "3/2";
	}

	$tempos = sizeof($durações);
	$unidade = $durações[0];

	return "{$tempos}/{$unidade}";
}
