<?php


function mesma_coluna_ou_mesma_linha($posicao_do_rei, $posicao_do_atacante){
    return ($posicao_do_rei[0] == $posicao_do_atacante[0] || $posicao_do_rei[1] == $posicao_do_atacante[1]);
}

function mesma_diagonal($posicao_do_rei, $posicao_do_atacante){
   return (
   abs(ord($posicao_do_rei[0]) - ord($posicao_do_atacante[0])) ==
   abs(ord($posicao_do_rei[1]) - ord($posicao_do_atacante[1])) );
}

function cheque_o_xeque($posicao_do_rei, $posicao_do_atacante, $peca_atacante){

    if ($peca_atacante == "bispo" && mesma_diagonal($posicao_do_rei, $posicao_do_atacante))
            return "xeque";

    if ($peca_atacante == "torre" || (mesma_coluna_ou_mesma_linha($posicao_do_rei, $posicao_do_atacante))
        return "xeque";

    if($peca_atacante=="cavalo") return "xeque";

    return "não xeque";


    }

