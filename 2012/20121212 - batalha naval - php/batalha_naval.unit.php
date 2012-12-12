<?php

include "batalha_naval.php";

class TestBatalhaNaval extends PHPUnit_Framework_TestCase {

    public function test_tiro_acerta(){
        $tabuleiro = array(
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            );

        $jogo = new BatalhaNaval();
        $jogo->insereNavio(array(1,1), array(1,3));

        $this->assertSame($tabuleiro, $jogo->$tabuleiro);
    }
}