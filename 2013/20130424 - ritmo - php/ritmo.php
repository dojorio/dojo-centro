<?php

function ritmo($durações) {
	$tempos = 0;
	$unidade = max($durações);
	foreach ($durações as $duração)
		$tempos += $unidade / $duração;
	return "{$tempos}/{$unidade}";
}
