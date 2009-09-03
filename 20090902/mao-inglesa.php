<?php
function complementar_a_7($o_array){
	
	$novo_array = array_map(
		create_function('$numero','return 7 - $numero;'),
		$o_array
	);
	sort($novo_array);
	
	return $novo_array;
}

function fechador_de_sinais($sinal_aberto){
	$fechados = array(
		1 => array(3, 4, 5),
		2 => array(3, 6),
		3 => array(1, 2, 6)
	);
	
	if (!$fechados[$sinal_aberto]) {	
		return complementar_a_7($fechados[7 - $sinal_aberto]);
	}
	return $fechados[$sinal_aberto];
}

?>
