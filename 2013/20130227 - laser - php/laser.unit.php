<?php

include "laser.php";

/*
|    |  | 
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
			new Inimigo(0, 0)
		);
		$this->assertSame(1, laser($tabuleiro));
	}

	function test_tabuleiro_com_dois_inimigos() {
		$tabuleiro = array(
			new Inimigo(0, 0),
			new Inimigo(1, 1)
		);
		$this->assertSame(2, laser($tabuleiro));
	}

	function test_tabuleiro_com_dois_inimigos_em_coluna() {
		$tabuleiro = array(
			new Inimigo(0, 0),
			new Inimigo(1, 0)
		);
		$this->assertSame(1, laser($tabuleiro));
	}

	function test_tabuleiro_com_dois_inimigos_em_linha() {
		$tabuleiro = array(
			new Inimigo(0, 0),
			new Inimigo(0, 1)
		);
		$this->assertSame(1, laser($tabuleiro));
	}

	function test_tabuleiro_com_tres_inimigos_em_coluna() {
		$tabuleiro = array(
			new Inimigo(0, 0),
			new Inimigo(1, 0),
			new Inimigo(2, 0),
		);
		$this->assertSame(1, laser($tabuleiro));
	}

	function test_tabuleiro_com_tres_inimigos_em_duas_colunas() {
		$tabuleiro = array(
			new Inimigo(0, 1),
			new Inimigo(1, 0),
			new Inimigo(2, 0),
		);
		$this->assertSame(2, laser($tabuleiro));
	}

	function test_tabuleiro_com_tres_inimigos_em_tres_colunas() {
		$tabuleiro = array(
			new Inimigo(0, 1),
			new Inimigo(1, 0),
			new Inimigo(2, 2),
		);
		$this->assertSame(3, laser($tabuleiro));
	}

	function test_tabuleiro_com_tres_inimigos_em_duas_colunas_2() {
		$tabuleiro = array(
			new Inimigo(0, 0),
			new Inimigo(1, 0),
			new Inimigo(2, 2),
		);
		$this->assertSame(2, laser($tabuleiro));
	}

	function test_tabuleiro_com_seis_inimigos_em_tres_linhas_tres_colunas() {
		$tabuleiro = array(
			new Inimigo(0, 1),
			new Inimigo(0, 2),
			new Inimigo(0, 3),
			new Inimigo(1, 0),
			new Inimigo(2, 0),
			new Inimigo(3, 0),
		);
		$this->assertSame(2, laser($tabuleiro));
	}	

	function test_tabuleiro_com_seis_inimigos() {
		$tabuleiro = array(
			new Inimigo(0, 1),
			new Inimigo(1, 0),
			new Inimigo(1, 1),
			new Inimigo(1, 2),
			new Inimigo(2, 2),
			new Inimigo(3, 0),
		);
		$this->assertSame(3, laser($tabuleiro));
	}	

	function test_tabuleiro_com_seis_inimigos_transpostos() {
		$tabuleiro = array(
			new Inimigo(1, 0),
			new Inimigo(0, 1),
			new Inimigo(1, 1),
			new Inimigo(2, 1),
			new Inimigo(2, 2),
			new Inimigo(0, 3),
		);
		$this->assertSame(3, laser($tabuleiro));
	}	
}