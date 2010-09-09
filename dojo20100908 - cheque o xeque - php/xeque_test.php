<?php
/**
* executar teste
* @example $ phpunit --colors xeque_test.php
* @fonte http://phpunit.de
*/
require_once 'PHPUnit/Framework.php';
require_once 'xeque.php';

function xeque_torre($posicao_do_rei, $posicao_do_atacante) {
    return cheque_o_xeque($posicao_do_rei, $posicao_do_atacante, "torre");
}

function xeque_bispo($posicao_do_rei, $posicao_do_atacante) {
    return cheque_o_xeque($posicao_do_rei, $posicao_do_atacante, "bispo");
}

function xeque_cavalo($posicao_do_rei, $posicao_do_atacante) {
    return cheque_o_xeque($posicao_do_rei, $posicao_do_atacante, "cavalo");
}

function xeque_dama($posicao_do_rei, $posicao_do_atacante) {
    return xeque_torre($posicao_do_rei, $posicao_do_atacante) || xeque_bispo($posicao_do_rei, $posicao_do_atacante);
}


class XequeTest extends PHPUnit_Framework_TestCase{


    public function test_Rei_na_e1_Torre_na_e5_eh_xeque(){
        $this->assertEquals(xeque_torre("e1", "e5"), "xeque");
    }

    public function test_Rei_na_e1_Torre_na_c5_nao_eh_xeque(){
        $this->assertEquals(xeque_torre("e1", "c5"), "não xeque");
    }
    public function test_Rei_na_e1_Torre_na_a1_eh_xeque(){
        $this->assertEquals(xeque_torre("e1", "a1"), "xeque");
    }
    public function test_Rei_na_e1_Torre_na_c1_eh_xeque(){
        $this->assertEquals(xeque_torre("e1", "c1"), "xeque");
    }
    public function test_Rei_na_e1_Torre_na_c4_nao_eh_xeque(){
        $this->assertEquals(xeque_torre("e1", "c4"), "não xeque");
    }
    public function test_Rei_na_d2_Torre_na_d4_eh_xeque(){
        $this->assertEquals(xeque_torre("d2", "d4"), "xeque");
    }
    public function test_Rei_na_c1_Bispo_na_f4_eh_xeque(){
        $this->assertEquals(xeque_bispo("c1", "f4"), "xeque");
    }

    public function test_Rei_na_c1_Bispo_na_b2_eh_xeque(){
        $this->assertEquals(xeque_bispo("c1", "b2"), "xeque");
    }
    public function test_Rei_na_c1_Bispo_na_b3_nao_eh_xeque(){
        $this->assertEquals(xeque_bispo("c1", "b3"), "não xeque");
    }
    public function test_Rei_na_c1_Bispo_na_b4_nao_eh_xeque(){
        $this->assertEquals(xeque_bispo("c1", "b4"), "não xeque");
    }
    public function test_Rei_na_d4_Bispo_na_b2_eh_xeque(){
        $this->assertEquals(xeque_bispo("d4", "b2"), "xeque");
    }
    public function test_Rei_na_c1_Dama_na_b3_nao_eh_xeque(){
        $this->assertEquals(xeque_dama("c1", "b3"), "não xeque");
    }
    public function test_Rei_na_d4_Dama_na_b3_eh_xeque(){
        $this->assertEquals(xeque_dama("d4", "b3"), "xeque");
    }
    public function test_Rei_na_b4_Dama_na_b3_eh_xeque(){
        $this->assertEquals(xeque_dama("b4", "b3"), "xeque");
    }
    public function test_Rei_na_c2_Dama_na_e2_eh_xeque(){
        $this->assertEquals(xeque_dama("c2", "e2"), "xeque");
    }
    public function test_Rei_na_c2_Cavalo_na_d4_eh_xeque(){
        $this->assertEquals(xeque_cavalo("c2", "d4"), "xeque");
    }
    public function test_Rei_na_c2_Cavalo_na_c4_nao_eh_xeque(){
        $this->assertEquals(xeque_cavalo("c2", "c4"), "não xeque");
    }

}
?>

