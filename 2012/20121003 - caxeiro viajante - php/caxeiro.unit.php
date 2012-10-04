<?php

require_once "caxeiro.php";

class TestCaxeiro extends PHPUnit_Framework_TestCase {

    public function test_duasCidades() {
        $cidades = array(
            'A' => array('B' => 1),
            'B' => array('A' => 1),
        );
        
        $this->assertEquals(2, caixeiro($cidades));
    }
    
    public function test_duasCidadesComPesos2() {
        $cidades = array(
            'A' => array('B' => 2),
            'B' => array('A' => 2),
        );
        
        $this->assertEquals(4, caixeiro($cidades));
    }
    
    public function test_duasCidadesComPesosDiferentes() {
        $cidades = array(
            'A' => array('B' => 1),
            'B' => array('A' => 2),
        );
        
        $this->assertEquals(3, caixeiro($cidades));
    }
    
    public function test_tresCidades() {
        $cidades = array(
            'A' => array('B' => 1),
            'B' => array('C' => 1),
            'C' => array('A' => 2),
        );
        
        $this->assertEquals(4, caixeiro($cidades));
    }
    
    public function test_tresCidades2() {
        $cidades = array(
            'A' => array('B' => 1),
            'B' => array('C' => 2),
            'C' => array('A' => 3),
        );
        
        $this->assertEquals(6, caixeiro($cidades));
    }
    
    public function test_quatroCidades() {
        $cidades = array(
            'A' => array('B' => 1),
            'B' => array('C' => 2),
            'C' => array('D' => 3),
            'D' => array('A' => 4),
        );
        
        $this->assertEquals(10, caixeiro($cidades));
    }
    
    public function test_quatroCidadesComOutraOrdem() {
        $cidades = array(
            'A' => array('C' => 1),
            'C' => array('B' => 2),
            'B' => array('D' => 3),
            'D' => array('A' => 4),
        );
        
        $this->assertEquals(10, caixeiro($cidades));
    }
    
    
    public function test_cincoCidades() {
        $cidades = array(
            'A' => array('B' => 1),
            'B' => array('C' => 2),
            'C' => array('D' => 3),
            'D' => array('E' => 6),
            'E' => array('A' => 6),
        );
        
        $this->assertEquals(18, caixeiro($cidades));
    }
    
    public function test_quatroCidadesCompleto() {
        $cidades = array(
            'A' => array('B' => 1, 'C' => 5, 'D' => 4),
            'B' => array('C' => 2, 'A' => 1, 'D' => 6),
            'C' => array('D' => 3, 'B' => 2, 'A' => 5),
            'D' => array('A' => 4, 'B' => 6, 'C' => 3),
        );
        
        $this->assertEquals(10, caixeiro($cidades));
    }
    
    public function test_tresCidadesCompleto() {
        $cidades = array(
            'A' => array('B' => 4, 'C' => 2),
            'B' => array('A' => 3, 'C' => 5),
            'C' => array('A' => 6, 'B' => 1),
        );
        
        $this->assertEquals(6, caixeiro($cidades));
    }
}
