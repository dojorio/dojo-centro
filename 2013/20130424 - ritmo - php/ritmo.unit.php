<?php

require "ritmo.php";

class RitmoTest extends PHPUnit_Framework_TestCase {

  function test_um_por_um() {
    $durações = array(1);
    $this->assertSame('1/1', ritmo($durações));
  }

  function test_um_por_dois() {
    $durações = array(2);
    $this->assertSame('1/2', ritmo($durações));
  }

  function test_dois_por_um() {
    $durações = array(1, 1);
    $this->assertSame('2/1', ritmo($durações));
  }

  function test_tres_por_dois() {
    $durações = array(1, 2);
    $this->assertSame('3/2', ritmo($durações));
  }

  function test_tres_por_um() {
    $durações = array(1, 1, 1);
    $this->assertSame('3/1', ritmo($durações));
  }

  function test_tres_por_dois_outro() {
    $durações = array(2, 1);
    $this->assertSame('3/2', ritmo($durações));
  }

  function test_cinco_por_quatro() {
    $durações = array(1, 4);
    $this->assertSame('5/4', ritmo($durações));
  }

  function test_sete_por_quatro() {
    $durações = array(1, 2, 4);
    $this->assertSame('7/4', ritmo($durações));
  }

  function test_seis_por_dois() {
    $durações = array(1, 2, 4);
    $this->assertSame('7/4', ritmo($durações));
  }


}
