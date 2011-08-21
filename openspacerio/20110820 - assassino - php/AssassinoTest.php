<?php
/*http://dojopuzzles.com/problemas/exibe/descubra-o-assassino */

DEFINE("ASSASSINO",2);
DEFINE("LOCAL",3);
DEFINE("ARMA",4);
require 'Assassino.php';

class AssassinoTest extends PHPUnit_Framework_TestCase{

  /**
   * @var Investigacao
   */
  public $investigacao;

  function setup() {
    $this->investigacao = new Investigacao;
    $this->investigacao->setTeoria(ASSASSINO, LOCAL, ARMA);
  }

  function testTudoCerto(){
    $this->assertEquals(0, $this->investigacao->respostaTestemunha(ASSASSINO,LOCAL,ARMA));
  }

  function testSoAssassinoErrado(){
    $this->assertNotEquals(0, $this->investigacao->respostaTestemunha(ASSASSINO-1,LOCAL,ARMA));
    $this->assertNotEquals(2, $this->investigacao->respostaTestemunha(ASSASSINO-1,LOCAL,ARMA));
    $this->assertNotEquals(3, $this->investigacao->respostaTestemunha(ASSASSINO-1,LOCAL,ARMA)); 
  }

  function testSoLocalErrado(){
    $this->assertNotEquals(0, $this->investigacao->respostaTestemunha(ASSASSINO,LOCAL-1,ARMA));
    $this->assertNotEquals(1, $this->investigacao->respostaTestemunha(ASSASSINO,LOCAL-1,ARMA));
    $this->assertNotEquals(3, $this->investigacao->respostaTestemunha(ASSASSINO,LOCAL-1,ARMA)); 
  }

  function testSoArmaErrada(){
    $this->assertNotEquals(0, $this->investigacao->respostaTestemunha(ASSASSINO,LOCAL,ARMA-1));
    $this->assertNotEquals(1, $this->investigacao->respostaTestemunha(ASSASSINO,LOCAL,ARMA-1));
    $this->assertNotEquals(2, $this->investigacao->respostaTestemunha(ASSASSINO,LOCAL,ARMA-1)); 
  }

  function testErroEntreAssassinoLocal(){
    $this->assertNotEquals(3, $this->investigacao->respostaTestemunha(ASSASSINO-1,LOCAL-1,ARMA));
    $this->assertNotEquals(0, $this->investigacao->respostaTestemunha(ASSASSINO-1,LOCAL-1,ARMA));
  }

  function testErroEntreAssassinoArma(){
    $this->assertNotEquals(2, $this->investigacao->respostaTestemunha(ASSASSINO-1,LOCAL,ARMA-1));
    $this->assertNotEquals(0, $this->investigacao->respostaTestemunha(ASSASSINO-1,LOCAL,ARMA-1));
  }

  function testErroEntreLocalArma(){
    $this->assertNotEquals(1, $this->investigacao->respostaTestemunha(ASSASSINO,LOCAL-1,ARMA-1));
    $this->assertNotEquals(0, $this->investigacao->respostaTestemunha(ASSASSINO,LOCAL-1,ARMA-1));
  }

  function testErroTodos() {
    $this->assertNotEquals(0, $this->investigacao->respostaTestemunha(ASSASSINO-1,LOCAL-1,ARMA-1));
  }
}
