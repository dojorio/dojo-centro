<?php

function maior_nota_menor_que_o_valor($valor, $notas){
    $notas = array_filter($notas, function($nota) use ($valor) {
        return $nota <= $valor;
    });
    
    return !empty($notas) ? max($notas) : 0;
}

function troco($valor, $notas = array(100, 50, 10, 5, 1)) {
    if ($valor <= 0)
        return array();
    
    $maior_nota = maior_nota_menor_que_o_valor($valor, $notas);
    
    if ($maior_nota == 0)
        return array();


    if ((troco($valor - $maior_nota, $notas)) >= min($notas)) {
        return array_merge(array($maior_nota), troco($valor - $maior_nota, $notas));
    } else {
        unset($notas[array_search($maior_nota, $notas)]);
        return array_merge(array($maior_nota), troco($valor - $maior_nota, $notas));
    
    }

    $resultado = array_merge(array($maior_nota), troco($valor - $maior_nota, $notas));


}

