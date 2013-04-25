<?php
function gcd($a, $b) {
    if ($a == 0 || $b == 0)
        return abs( max(abs($a), abs($b)) );

    $r = $a % $b;
    return ($r != 0) ?
        gcd($b, $r) :
        abs($b);
}

function ritmo($durações) {
	$tempos = 0;
	$unidade = max($durações);
	foreach ($durações as $duração)
		$tempos += $unidade / $duração;
	$gcd = gcd($tempos, $unidade);
	$tempos /= $gcd;
	$unidade /= $gcd;
	return "{$tempos}/{$unidade}";
}
