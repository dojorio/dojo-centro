<?php

include "laser.php";

/*
     |  | 
|    |  x
---x----x--
|    |  |     
-    x  x  |
--x--x--x--|
|----|--|--|
*/

class LaserTest extends PHPUnit_Framework_TestCase {

	function test_tabuleiro_vazio() {
		$tabuleiro = array();
		$this->assertSame(0, laser($tabuleiro));
	}

	function test_tabuleiro_com_um_inimigo() {
		$tabuleiro = array(
			array(0, 0)
		);
		$this->assertSame(1, laser($tabuleiro));
	}

	function test_tabuleiro_com_dois_inimigos() {
		$tabuleiro = array(
			array(0, 0),
			array(1, 1)
		);
		$this->assertSame(2, laser($tabuleiro));
	}

	function test_tabuleiro_com_dois_inimigos_em_coluna() {
		$tabuleiro = array(
			array(0, 0),
			array(1, 0)
		);
		$this->assertSame(1, laser($tabuleiro));
	}

	function test_tabuleiro_com_dois_inimigos_em_linha() {
		$tabuleiro = array(
			array(0, 0),
			array(0, 1)
		);
		$this->assertSame(1, laser($tabuleiro));
	}

}