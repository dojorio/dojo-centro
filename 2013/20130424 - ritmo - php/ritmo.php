<?php

function ritmo($durações) {
	if (count($durações) == 1) {
		$tempos = count($durações);
		$unidade = $durações[0];
	} else {
		$tempos = array_sum($durações);
		$unidade = max($durações);
	}
	return "{$tempos}/{$unidade}";
}
