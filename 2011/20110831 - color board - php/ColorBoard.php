<?php

class ColorBoard {
	private $board;
	
	public function ColorBoard($board) {
		$this->board = $board;
	}
	
	private function magicWand($row, $column, $value) {
		if ($this->shouldErase($row, $column, $value)) {
			$this->board[$row][$column] = null;
			$this->magicWand($row, $column+1, $value);
			$this->magicWand($row, $column-1, $value);
		}
	}
	
	private function shouldErase($row, $column, $value) {
		return isset($this->board[$row][$column]) && $this->board[$row][$column] == $value;
	}
	
	
	public function click($row, $column) {
		$clicked = $this->board[$row][$column];
		
		$direita = $this->shouldErase($row, $column + 1, $clicked);
		$esquerda = $this->shouldErase($row, $column - 1, $clicked);
		
		if ($direita OR $esquerda)
			$this->magicWand($row, $column, $clicked);
	}
	
	public function getBoard() {
		return $this->board;
	}
	
}


