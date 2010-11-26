<?php
/**
* executar teste
* @example $ phpunit --colors espiral_test.php
* @fonte http://phpunit.de
*/
require_once 'PHPUnit/Framework.php';
require_once 'espiral.php';

class EspiralTest extends PHPUnit_Framework_TestCase
{
    public function testUmElemento()
    {
	    $espiral = "1";
        $this->assertEquals($espiral, gerar_espiral(1));
    }

    public function testQuatroElementos()
    {
    	$espiral  = "1 2\n";
	    $espiral .= "4 3";
        $this->assertEquals($espiral, gerar_espiral(4));
    }

    public function testNoveElementos()
    {
    	$espiral  = "1 2 3\n";
    	$espiral .= "8 9 4\n";
	    $espiral .= "7 6 5";
        $this->assertEquals($espiral, gerar_espiral(9));
    }

}
?>

