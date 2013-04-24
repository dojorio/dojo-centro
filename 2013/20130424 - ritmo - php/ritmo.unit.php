<?php

include "ritmo.php";


class RitmoTest extends PHPUnit_Framework_TestCase {
	function test_um_por_um() {
		$figuras = array(1);
		$this->assertSame(1/1, ritmo($figuras));
	}

}
