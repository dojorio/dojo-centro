<?php

function ritmo($durações) {
	if (count(array_unique($durações)) == 2) {
		$tempos = array_sum($durações);
		$unidade = max($durações);
	} else {
		$tempos = count($durações);
		$unidade = $durações[0];
	}
	return "{$tempos}/{$unidade}";
}
