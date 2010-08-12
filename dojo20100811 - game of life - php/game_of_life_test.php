<?php
/**
* executar teste
* @example $ phpunit --colors game_of_life_test.php
* @fonte http://phpunit.de
*/
require_once 'PHPUnit/Framework.php';
require_once 'game_of_life.php';

class JogoDaVidaTest extends PHPUnit_Framework_TestCase
{
    public function test_celula_morre_na_primeira_posicao_sem_vizinhos(){
        $ambiente = array(1,0);
                $this->assertEquals(array(0,0), game_of_life($ambiente));
    }

    public function test_celula_morre_com_menos_de_dois_vizinhos(){
        $celula = new Celula();
        $celula->vizinhosVivos(0);
        $this->assertFalse($celula->viva);
        $celula->vizinhosVivos(1);
        $this->assertFalse($celula->viva);
    }

    public function test_celula_revive_com_tres_vizinhos(){
        $celula = new Celula();
        $celula->viva = false;
        $celula->vizinhosVivos(3);
        $this->assertTrue($celula->viva);
    }

    public function test_celula_morre_com_mais_de_tres_vizinhos(){
        $celula = new Celula();
        $celula->vizinhosVivos(4);
        $this->assertFalse($celula->viva);
    }

    public function test_celula_vive_com_dois_vizinhos(){
        $celula = new Celula();
        $celula->vizinhosVivos(2);
        $this->assertTrue($celula->viva);
    }

    public function test_celula_morta_com_dois_vizinhos_continua_morta(){
        $celula = new Celula();
        $celula->viva = false;
        $celula->vizinhosVivos(2);
        $this->assertFalse($celula->viva);
    }


}

?>

