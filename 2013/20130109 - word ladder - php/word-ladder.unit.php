<?php

require_once "word-ladder.php";

class TestWordLadder extends PHPUnit_Framework_TestCase {
    
    public function test_casa() {
        $palavras = array('casa');
        $this->assertEquals(1, wordLadder($palavras));
    }
    
    public function test_casa_cama() {
        $palavras = array('casa', 'cama');
        $this->assertEquals(2, wordLadder($palavras));
    }
    
    public function test_casa_bola() {
        $palavras = array('casa', 'bola');
        $this->assertEquals(1, wordLadder($palavras));
    }
    
    public function test_casa_saco() {
        $palavras = array('casa', 'saco');
        $this->assertEquals(1, wordLadder($palavras));
    }

    public function test_casa_cada() {
        $palavras = array('casa', 'cada');
        $this->assertEquals(2, wordLadder($palavras));
    }

    public function test_casa_cada_cama() {
        $palavras = array('casa', 'cada', 'cama');
        $this->assertEquals(3, wordLadder($palavras));
    }

    public function test_casa_cada_bola() {
        $palavras = array('casa', 'cada', 'bola');
        $this->assertEquals(2, wordLadder($palavras));
    }

    public function test_casa_bola_cada() {
        $palavras = array('casa', 'bola', 'cada');
        $this->assertEquals(2, wordLadder($palavras));
    }

    public function test_fato_pato_moda() {
        $palavras = array('fato', 'pato', 'moda');
        $this->assertEquals(2, wordLadder($palavras));
    }

    public function test_fato_pato_moda_rato() {
        $palavras = array('fato', 'pato', 'moda', 'rato');
        $this->assertEquals(3, wordLadder($palavras));
    }

    public function test_moda_fato_pato_rato() {
        $palavras = array('moda', 'fato', 'pato', 'rato');
        $this->assertEquals(3, wordLadder($palavras));
    }

    public function test_moda_fato_pato_rato_raso() {
        $palavras = array('moda', 'fato', 'pato', 'rato', 'raso');
        $this->assertEquals(4, wordLadder($palavras));
    }
}

