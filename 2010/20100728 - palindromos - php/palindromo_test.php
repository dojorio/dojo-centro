<?php
/**
* executar teste
* @example $ phpunit --colors palindromo_test.php
* @fonte http://phpunit.de
*/
require_once 'PHPUnit/Framework.php';
require_once 'palindromo.php';

class PalindromoTest extends PHPUnit_Framework_TestCase
{
    public function test_1_eh_um_palindromo(){
        $this->assertEquals(palindromizar(1), Array('numero de passos' => 0, 'resultado'=>1));
    }

    public function test_um_digito_sempre_eh_palindromo(){
        $this->assertEquals(palindromizar(5), Array('numero de passos' => 0, 'resultado'=>5));
    }

    public function test_palindromo_dois_digitos(){
        $this->assertEquals(palindromizar(11), Array('numero de passos' => 0, 'resultado'=>11));
    }

    public function test_eh_palindromo_um_digito(){
        $this->assertEquals(eh_palindromo(7), true);
    }

    public function test_10_nao_eh_palindromo(){
        $this->assertEquals(eh_palindromo(10), false);
    }

    public function test_9_eh_palindromo(){
        $this->assertEquals(eh_palindromo(9), true);
    }

    public function test_13_nao_eh_palindromo(){
        $this->assertEquals(eh_palindromo(13), false);
    }

    public function test_10_vira_palindromo_em_1_passo(){
        $this->assertEquals(palindromizar(10), Array('numero de passos' => 1,'resultado'=>11));

    }

    public function test_12_vira_palindromo_em_1_passo(){
        $this->assertEquals(palindromizar(12), Array('numero de passos' => 1, 'resultado'=>33));
    }

    public function test_20_vira_palindromo_em_1_passo(){
        $this->assertEquals(palindromizar(20), Array('numero de passos' => 1, 'resultado'=>22));
    }

    public function test_700_vira_palindromo_em_1_passo(){
        $this->assertEquals(palindromizar(700), Array('numero de passos' => 1, 'resultado'=>707));
    }

    public function test_102_vira_palindromo_em_1_passo(){
        $this->assertEquals(palindromizar(102), Array('numero de passos' => 1, 'resultado'=>303));
    }

    public function test_19_vira_palindromo_em_2_passos(){
        $this->assertEquals(palindromizar(19), Array('numero de passos' => 2, 'resultado'=>121));
    }
    public function test_195_vira_palindromo_em_4_passos(){
        $this->assertEquals(palindromizar(195), Array('numero de passos' => 4, 'resultado'=>9339));
    }
}

?>

