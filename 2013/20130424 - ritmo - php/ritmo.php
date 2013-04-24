<?php

function ritmo($durações) {
	$tempos = array_sum(array_unique($durações));
	$unidade = max($durações);

	return "{$tempos}/{$unidade}";
}
