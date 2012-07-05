<?php

require_once "matriz-espiral.php";

class TestMatrizEspiral extends PHPUnit_Framework_TestCase {
    
    function test1x1() {  
        $esperado = array(array(1));     
        $this->assertEquals($esperado, matrizEspiral(1, 1));
    }
    
    function test1x2() {  
        $esperado = array(array(1, 2));     
        $this->assertEquals($esperado, matrizEspiral(1, 2));
    }
    
    function test1x3() {  
        $esperado = array(array(1, 2, 3));     
        $this->assertEquals($esperado, matrizEspiral(1, 3));
    }
     
    function test2x1() {  
        $esperado = array(array(1),array(2));     
        $this->assertEquals($esperado, matrizEspiral(2, 1));
    }
    
    function test2x2() {  
        $esperado = array(array(1, 2),array(4, 3));     
        $this->assertEquals($esperado, matrizEspiral(2, 2));
    }
    
    function test2x3() {  
        $esperado = array(
            array(1, 2, 3),
            array(6, 5, 4));     
        $this->assertEquals($esperado, matrizEspiral(2, 3));
    }
    
    function test3x1() {  
        $esperado = array(
            array(1),
            array(2),            
            array(3));     
        $this->assertEquals($esperado, matrizEspiral(3, 1));
    }
    
    function test3x2() {  
        $esperado = array(
            array(1, 2),
            array(6, 3),            
            array(5, 4));     
        $this->assertEquals($esperado, matrizEspiral(3, 2));
    }
    
}

