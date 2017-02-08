exports.problem = function (map) {
    if (!map[0].includes('A')) {
    	return 0
    } 

    var primeira_posFumaca = map[0].indexOf('*')
    var ultima_posAeroporto = map[0].lastIndexOf("A")

    var ultima_posFumaca = map[0].lastIndexOf('*')
    var primeira_posAeroporto = map[0].indexOf("A")
    var posFumaca, posAeroporto;

    if ( primeira_posFumaca == ultima_posFumaca ) {
    	posFumaca = ultima_posFumaca 
    }
    else
    {
    	posFumaca = ultima_posFumaca 
    }

    if ( primeira_posAeroporto == ultima_posAeroporto ) {
    	posAeroporto = primeira_posAeroporto
    } else  {
    	posAeroporto = primeira_posAeroporto
    }



    	var direita = posAeroporto+1;
    	var esquerda = posAeroporto-1;

    	while(!(direita >= map[0].length && esquerda < 0)){
    		if(direita <= map[0].length){
    			if (map[0][direita] === '*'){
    				return direita - posAeroporto;
    			}
    			direita++;
    		}
    		if (esquerda >= 0){
    			if (map[0][esquerda] == '*'){
    				return posAeroporto - esquerda;
    			} 
    			esquerda--;
    		}
    	}

   

	return 0;
    
};
