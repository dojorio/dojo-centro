<?php

function inverso($numero){
	return 1 / $numero;
}

function ritmo($durações) {
	$unidade = max($durações);
	$tempos = array_sum(array_map('inverso', $durações)) * $unidade;
	return "{$tempos}/{$unidade}";
}
