<?php

function laser($inimigos) {
	if (isset($inimigos[1]) and (
			$inimigos[1][1] == $inimigos[0][1] or 
			$inimigos[1][0] == $inimigos[0][0] ))
		return 1;
	return count($inimigos);
}