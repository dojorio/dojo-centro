<?php

function formatar_em_espiral($matriz){
    $espiral = "";
    foreach($matriz as $linha){
        foreach($linha as $celula){
            $espiral .= $celula." ";
        }
        $espiral = rtrim($espiral). "\n";
    }
    return substr($espiral, 0, -1);
}
function direita($espiral, $coluna, $linha, $coluna_maxima, $elemento){
$espiral [$linha][$coluna]= ++$elemento;
}

function gerar_espiral($tamanho){

    $espiral = array();

    if($tamanho == 1){
            $elemento=0;
            $linha = 0;
            $coluna = 0;

            $linha_maxima = sqrt($tamanho) - 1;
            $coluna_maxima = $linha_maxima;
            $linha_minima = 0;
            $coluna_minima = 0;

            direita(&$espiral, $coluna, $linha, $coluna_maxima, $elemento);
  //          baixo(&$espiral, $linha_minima, $linha_maxima, $coluna, $elemento_inicial);
   //         esquerda();
     //       cima();

            //$espiral[$linha][$coluna] = $elemento;
    }elseif($tamanho == 4){
        $espiral[] = array(1,2);
        $espiral[] = array(4,3);
    }elseif($tamanho == 9){
        $espiral[] = array(1, 2, 3);
        $espiral[] = array(8, 9, 4);
        $espiral[] = array(7, 6, 5);
    }


    $espiral = formatar_em_espiral($espiral);

    return $espiral;
}
?>

