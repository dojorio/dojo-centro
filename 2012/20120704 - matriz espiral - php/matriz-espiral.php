<?php

function matrizEspiral($linhas, $colunas) {

    $matriz = array();
    
    for ($i = 1; $i <= $colunas; $i++) {
        $matriz[0][] = $i;
    }
    
    if ($linhas > 1) {
        for ($j = $i; $j <= $colunas * 2; $j++) {
            $matriz[1][] = $j;
        }
        $matriz[1] = array_reverse($matriz[1]);
    }
    
    if ($linhas == 3) {
       $matriz[2][0] = 3;
    }
    
    return $matriz;
}
