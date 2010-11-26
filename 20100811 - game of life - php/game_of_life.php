<?php

function game_of_life($matriz)
{
    return array(0,0);

}

class Celula{

    public $viva = true;

    public function vizinhosVivos($vizinhos){

        $this->viva = ($vizinhos == 3) || ($vizinhos == 2) && $viva;

    }

}

