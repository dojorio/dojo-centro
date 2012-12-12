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
		if($this->tabuleiro[$x][$y] == 1){
			$this->status = "navio acertado";
		}
		return $this->tabuleiro[$x][$y] == 1;
	}
}