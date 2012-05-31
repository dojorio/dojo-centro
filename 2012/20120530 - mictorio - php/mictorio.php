<?php

define('OCUPADO', 1);
define('LIVRE', 0);

function posicaoAceitavel($mictorios, $posicao) {
    return  !isset($mictorios[$posicao]) || $mictorios[$posicao] == LIVRE;
}

function escolheMictorio($mictorios) {

    $totalDeMictorios = count($mictorios);
    
    for ($i = 0; $i < $totalDeMictorios; $i++) {
        
        if ($mictorios[$i] == LIVRE) {
            if (posicaoAceitavel($mictorios, $i - 1) && posicaoAceitavel($mictorios, $i + 1)) {
                return $i;
            }
        }
    }
    
    if (in_array(LIVRE,$mictorios)) {
        return array_search(LIVRE, $mictorios);
    }

    return -1;

}
