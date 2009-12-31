<?php
require_once('simpletest/autorun.php');
require_once('kombat.php');

class TesteKombat extends UnitTestCase {

    function teste_resultado_de_um_turno_com_dano_bonus_zero() {
        $subzero = new Lutador(5, 2);
        $kabal = new Lutador(1, 4);
        $processadorTurnos = new ProcessadorTurnos();
        $resultado = $processadorTurnos->executarTurno($subzero, $kabal, 0, 0);
        $this->assertTrue($resultado);
    }
    
    function teste_resultado_de_um_turno_sem_dano_bonus_zero() {
        $subzero = new Lutador(1, 2);
        $kabal = new Lutador(2, 4);
        $processadorTurnos = new ProcessadorTurnos();
        $resultado = $processadorTurnos->executarTurno($subzero, $kabal, 0, 0);
        $this->assertFalse($resultado);
    }

    function teste_dano_de_um_turno_com_dano_5_bonus_zero() {
        $subzero = new Lutador(5, 2);
        $kabal = new Lutador(1, 4);
        $processadorTurnos = new ProcessadorTurnos();
        $processadorTurnos->executarTurno($subzero, $kabal, 0, 0);
        $dano = $processadorTurnos->pegaDanoDoUltimoTurno();
        $this->assertEqual(5, $dano);
    }
    
    function teste_dano_de_um_turno_com_dano_10_bonus_zero() {
        $subzero = new Lutador(5, 2);
        $kabal = new Lutador(1, 3);
        $processadorTurnos = new ProcessadorTurnos();
        $processadorTurnos->executarTurno($subzero, $kabal, 0, 0);
        $dano = $processadorTurnos->pegaDanoDoUltimoTurno();
        $this->assertEqual(10, $dano);
    }
    
    function teste_dano_de_um_turno_sem_dano_com_bonus_zero() {
        $subzero = new Lutador(3, 2);
        $kabal = new Lutador(1, 5);
        $processadorTurnos = new ProcessadorTurnos();
        $processadorTurnos->executarTurno($subzero, $kabal, 0, 0);
        $dano = $processadorTurnos->pegaDanoDoUltimoTurno();
        $this->assertEqual(0, $dano);
    }
}
?>
