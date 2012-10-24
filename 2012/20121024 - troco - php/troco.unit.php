<?php

require_once "troco.php";

// R$ 100,00, R$ 50,00, R$ 10,00, R$ 5,00 e R$ 1,00

class TestTroco extends PHPUnit_Framework_TestCase {

    public function test_troco_de_1_real() {
        $this->assertEquals(array(1), troco(1));
    }

    public function test_troco_de_5_reais() {
        $this->assertEquals(array(5), troco(5));
    }

    public function test_troco_de_10_reais() {
        $this->assertEquals(array(10), troco(10));
    }

    public function test_troco_de_2_reais() {
        $this->assertEquals(array(1 ,1), troco(2));
    }
    
    public function test_troco_de_20_reais(){
        $this->assertEquals(array(10, 10), troco(20));
    }
    
    public function test_troco_de_0_reais(){
        $this->assertEquals(array(), troco(0));
    }
    
    public function test_troco_de_30_reais(){
        $this->assertEquals(array(10, 10, 10), troco(30));
    }
    
    public function test_troco_de_40_reais(){
        $this->assertEquals(array(10, 10, 10, 10), troco(40));
    }
    
    public function test_troco_de_500_reais(){
        $this->assertEquals(array(100, 100, 100, 100, 100), troco(500));
    }
    
    public function test_troco_de_6_reais(){
        $this->assertEquals(array(5, 1), troco(6));
    }
    
    public function test_troco_de_21_reais(){
        $this->assertEquals(array(10, 10, 1), troco(21));
    }
    
    public function test_troco_de_21_reais_com_notas_embaralhadas(){
        $notas = array(1, 10);
        $this->assertEquals(array(10, 10, 1), troco(21, $notas));
    }
    
    public function test_troco_de_7_reais_com_notas_1_3_e_4(){
        $notas = array(1, 3, 4);
        $this->assertEquals(array(4, 3), troco(7, $notas));
    }
     
    public function test_troco_de_6_reais_com_notas_1_3_e_4(){
        $notas = array(1, 3, 4);
        $this->assertEquals(array(3, 3), troco(6, $notas));
    } 
    
    public function test_troco_de_21_reais_com_notas_10_5_e_2(){
        $notas = array(10, 5, 2);
        $this->assertEquals(array(10, 5, 2, 2, 2), troco(21, $notas));
    }
    
    
    
}
