<?php

class BatalhaNaval{

	public $status = "navio afundado";

	public function __construct(){
		$this->tabuleiro = array(
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        );
	}

	public function insereNavio($inicio,$fim){
		if($inicio[0]==$fim[0]){
			for($i=$inicio[1];$i<=$fim[1];$i++){
				$this->tabuleiro[$inicio[0]][$i] = 1;
			}
		}else{
			for($i=$inicio[0];$i<=$fim[0];$i++){
				$this->tabuleiro[$i][$inicio[1]] = 1;
			}
		}
	}
	

	public function tiro($x,$y){
		$acertou = $this->tabuleiro[$x][$y] == 1;
		$afundou = $x == 4 and $y == 2;
		if($acertou){
			$this->tabuleiro[$x][$y] = 'x';
			$this->status = "navio acertado";
			$afundou = $this->verificaAfundou($x, $y);
			if($afundou){
				$this->status = "navio afundado";
			}
		}
		return $acertou;
	}

	public function verificaAfundou($x, $y){
		$preX = $x - 1;
		$preY = $y - 1;
		$posX = $x + 1;
		$posY = $y + 1;

		if($preX >= 0)
			$preX = $this->tabuleiro[$preX][$y] == 1;
		else
			$preX = false;

		if($preY >= 0)
			$preY = $this->tabuleiro[$x][$preY] == 1;
		else
			$preY = false;

		if($posX < 10)
			$posX = $this->tabuleiro[$posX][$y] == 1;
		else
			$posX = false;

		if($posY < 10)
			$posY = $this->tabuleiro[$x][$posY] == 1;
		else
			$posY = false;

		return !$preX and !$preY and !$posX and !$posY;

	}
}