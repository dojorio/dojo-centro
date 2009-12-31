<?php
class Lutador{
    public $vida;
    
    public function __construct($ataque, $defesa) {
        $this->ataque = $ataque;
        $this->defesa = $defesa;
    }
}

class ProcessadorTurnos{
    
    public function executarTurno($atacante, $defensor, $bonus_ataque, $bonus_defesa){
        $this->atacante = $atacante;
        $this->defensor = $defensor;
        
        return $atacante->ataque > $defensor->defesa;
    }
    
    public function pegaDanoDoUltimoTurno() {
        $dano = 5 * ($this->atacante->ataque - $this->defensor->defesa);
        return $dano > 0 ? $dano : 0;
    }
}
?>
