<?php

function eh_palindromo($numero){
    return $numero == strrev($numero);
}

function palindromizar($numero){

    if (eh_palindromo($numero))
        return Array
        (
            'numero de passos' => 0,
            'resultado'=>$numero,
        );

    $resultado_do_passo = palindromizar($numero + strrev($numero));

    return Array
    (
        'numero de passos' => ($resultado_do_passo['numero de passos'] + 1),
        'resultado'=>$resultado_do_passo['resultado'],
    );
}


?>

