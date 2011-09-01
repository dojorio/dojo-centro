<?php

require_once './ColorBoard.php';

class DescribeColorBoard extends \PHPSpec\Context {
	
	function itShouldClearBoard() {
		$board = array(array(1, 1));
		
		$colorBoard = $this->spec(new ColorBoard($board));
		$colorBoard->click(0, 0);
		
		$expected = array(array(null, null));
		$colorBoard->getBoard()->should->be($expected);
	}
	
	function itShouldDoNothing() {
		$board = array(array(1, 2));
		
		$colorBoard = $this->spec(new ColorBoard($board));
		$colorBoard->click(0, 0);
		
		$expected = array(array(1, 2));
		$colorBoard->getBoard()->should->be($expected);
	}
	
	function itShouldBeAbleToClickOnTheLastColumnOfARow() {
		$board = array(array(1, 2));
		
		$colorBoard = $this->spec(new ColorBoard($board));
		$colorBoard->click(0, 1);
		
		$expected = array(array(1, 2));
		$colorBoard->getBoard()->should->be($expected);
	}
	
	function itShouldRemoveTheTwo2sClickingOnTheFirst() {
		$board = array(array(1, 2, 2));
		
		$colorBoard = $this->spec(new ColorBoard($board));
		$colorBoard->click(0, 1);
		
		$expected = array(array(1, null, null));
		$colorBoard->getBoard()->should->be($expected);
	}
	
	function itShouldRemoveTheTwo2sClickingOnTheFirstWithAnother2Before() {
		$board = array(array(2, 1, 2, 2));
		
		$colorBoard = $this->spec(new ColorBoard($board));
		$colorBoard->click(0, 3);
		
		$expected = array(array(2, 1, null, null));
		$colorBoard->getBoard()->should->be($expected);
	}
	
	function itShouldRemoveTheTwo2sClickingOnTheFirstWithAnother2After() {
		$board = array(array(2, 2, 1, 2));
		
		$colorBoard = $this->spec(new ColorBoard($board));
		$colorBoard->click(0, 0);
		
		$expected = array(array(null, null, 1, 2));
		$colorBoard->getBoard()->should->be($expected);
	}
	
}
