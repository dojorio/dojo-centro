<?php

require_once "word-ladder.php";

class TestWordLadder extends PHPUnit_Framework_TestCase {
    
    public function test_uma_palavra() {
        $palavras = array('casa');
        $this->assertEquals(1, wordLadder($palavras));
    }
    
    public function test_duas_palavras() {
        $palavras = array('casa', 'cama');
        $this->assertEquals(2, wordLadder($palavras));
    }
    
    public function test_duas_palavras_diferentes() {
        $palavras = array('casa', 'bola');
        $this->assertEquals(1, wordLadder($palavras));
    }
    
    public function test_duas_palavras_diferentes2() {
        $palavras = array('casa', 'saco');
        $this->assertEquals(1, wordLadder($palavras));
    }

}

