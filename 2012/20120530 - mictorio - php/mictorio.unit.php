<?php

require_once "mictorio.php";

class Test extends PHPUnit_Framework_TestCase {

	function testa_umMictorioLivre() {
	    $mictorios = array(LIVRE);
	    
		$this->assertSame(escolheMictorio($mictorios), 0);
	}
	
	function testa_umMictorioOcupado() {
	    $mictorios = array(OCUPADO);
	    
		$this->assertSame(escolheMictorio($mictorios), -1);	
	}
	
	function testa_doisMictoriosLivres() {
	    $mictorios = array(LIVRE, LIVRE);
	    
		$this->assertSame(escolheMictorio($mictorios), 0);	
	}
	
	
	function testa_doisMictoriosOcupados() {
	    $mictorios = array(OCUPADO, OCUPADO);
	    
		$this->assertSame(escolheMictorio($mictorios), -1);	
	}
	
	function testa_doisMictoriosUmLivreEUmOcupado() {
	    $mictorios = array(LIVRE, OCUPADO);
	    
		$this->assertSame(escolheMictorio($mictorios), 0);	
	}
	
	function testa_doisMictoriosUmOcupadoEUmLivre() {
	    $mictorios = array(OCUPADO, LIVRE);
	    
		$this->assertSame(escolheMictorio($mictorios), 1);	
	}
	
	function testa_LIVRE_LIVRE_OCUPADO() {
	    $mictorios = array(LIVRE, LIVRE, OCUPADO);
	    
		$this->assertSame(escolheMictorio($mictorios), 0);	
	}
	
	function testa_OCUPADO_LIVRE_LIVRE() {
	    $mictorios = array(OCUPADO, LIVRE, LIVRE);
	    
		$this->assertSame(escolheMictorio($mictorios), 2);	
	}
	
	function testa_OCUPADO_LIVRE_OCUPADO() {
	    $mictorios = array(OCUPADO, LIVRE, OCUPADO);
	    
		$this->assertSame(escolheMictorio($mictorios), 1);	
	}
	
	function testa_LIVRE_OCUPADO_LIVRE() {
	    $mictorios = array(LIVRE, OCUPADO, LIVRE);
	    
		$this->assertSame(escolheMictorio($mictorios), 0);	
	}
	
	function testa_LIVRE_OCUPADO_LIVRE_LIVRE() {
	    $mictorios = array(LIVRE, OCUPADO, LIVRE, LIVRE);
	    
		$this->assertSame(escolheMictorio($mictorios), 3);	
	}
	
	function testa_OCUPADO_OCUPADO_LIVRE_LIVRE() {
	    $mictorios = array(OCUPADO, OCUPADO, LIVRE, LIVRE);
	    
		$this->assertSame(escolheMictorio($mictorios), 3);	
	}
	
	
	function testa_OCUPADO_OCUPADO_LIVRE_OCUPADO() {
	    $mictorios = array(OCUPADO, OCUPADO, LIVRE, OCUPADO);
	    
		$this->assertSame(escolheMictorio($mictorios), 2);	
	}

    function testa_OCUPADO_OCUPADO_OCUPADO_LIVRE_OCUPADO_LIVRE_OCUPADO() {
	    $mictorios = array(OCUPADO, OCUPADO,OCUPADO, LIVRE, OCUPADO, LIVRE, OCUPADO);
	    
		$this->assertSame(escolheMictorio($mictorios), 3);	
	}
}

