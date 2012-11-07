<?php

include "caixa.php";

class TestCaixa extends PHPUnit_Framework_TestCase {


    public function test_nenhuma_caixa() {
        $caixas = array();
        $this->assertSame(0, empilha_caixas($caixas));
    }

    public function test_uma_caixa() {
        $caixas = array(new Caixa(2, 1));
        $this->assertSame(1, empilha_caixas($caixas));
    }

    public function test_duas_caixas() {
        $caixa1 = new Caixa(2, 1);
        $caixa2 = new Caixa(1, 1);

        $caixas = array($caixa1, $caixa2);
        $this->assertSame(2, empilha_caixas($caixas));
    }

    public function test_duas_caixas_que_nao_da() {
        $caixa1 = new Caixa(2, 1);
        $caixa2 = new Caixa(2, 1);

        $caixas = array($caixa1, $caixa2);
        $this->assertSame(1, empilha_caixas($caixas));
    }

    public function test_duas_caixas_em_ordem() {
        $caixa1 = new Caixa(2, 2);
        $caixa2 = new Caixa(2, 2);

        $caixas = array($caixa1, $caixa2);
        $this->assertSame(2, empilha_caixas($caixas));
    }

    public function test_tres_caixas_que_so_da_duas() {
        $caixas = array(new Caixa(1, 1), 
                        new Caixa(1, 1), 
                        new Caixa(1, 1));
        $this->assertSame(2, empilha_caixas($caixas));
    }

    public function test_tres_caixas_que_da() {
        $caixas = array(new Caixa(1, 2), 
                        new Caixa(1, 1), 
                        new Caixa(1, 1));
        $this->assertSame(3, empilha_caixas($caixas));
    }

    public function test_tres_caixas_que_empilha_duas() {
        $caixas = array(new Caixa(1, 1),
                        new Caixa(1, 1),
                        new Caixa(3, 1));
        $this->assertSame(2, empilha_caixas($caixas));
    }

    public function test_2_caixas_que_empilha_2() {
        $caixas = array(new Caixa(1, 1), 
                        new Caixa(2, 1)); 
                        
        $this->assertSame(2, empilha_caixas($caixas));
    }

    public function test_tres_caixas_que_empilha_duas_menores() {
        $caixas = array(new Caixa(1, 2),
                        new Caixa(1, 2),
                        new Caixa(3, 2));
        $this->assertSame(2, empilha_caixas($caixas));
    }
}