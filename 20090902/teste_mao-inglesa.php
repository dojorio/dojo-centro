<?php
require_once('simpletest/autorun.php');
require_once('mao-inglesa.php');

class TesteMaoInglesa extends UnitTestCase {
	function teste_sinal_1_abre_3_4_e_5_fecham() {
		$sinal_aberto = 1;
		$this->assertEqual(
			fechador_de_sinais($sinal_aberto),
			array(3,4,5));
	}
	
	function teste_sinal_2_abre_3_4_e_6_fecham() {
		$sinal_aberto = 2;
		$this->assertEqual(
			fechador_de_sinais($sinal_aberto),
			array(3,6));
	}
	
	function teste_sinal_3_abre_1_2_e_6_fecham() {
		$sinal_aberto = 3;
		$this->assertEqual(
			fechador_de_sinais($sinal_aberto),
			array(1,2,6));
	}
	
	function teste_sinal_4_abre_1_5_e_6_fecham() {
		$sinal_aberto = 4;
		$this->assertEqual(
			fechador_de_sinais($sinal_aberto),
			array(1,5,6));
	}
	
}
?>
