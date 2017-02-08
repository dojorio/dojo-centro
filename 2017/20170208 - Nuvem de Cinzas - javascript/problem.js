exports.problem = function (map) {
    if (!map[0].includes('A')) {
    	return 0
    } 

    var primeira_posFumaca = map[0].indexOf('*')
    var ultima_posAeroporto = map[0].lastIndexOf("A")

    var ultima_posFumaca = map[0].lastIndexOf('*')
    var primeira_posAeroporto = map[0].indexOf("A")
    
    if (primeira_posFumaca < ultima_posAeroporto) {

    	var direita = ultima_posAeroporto+1;
    	var esquerda= ultima_posAeroporto-1;

    	while(!(direita >= map[0].length && esquerda < 0)){
    		if(direita <= map[0].length){
    			if (map[0][direita] === '*'){
    				return direita - ultima_posAeroporto;
    			}
    			direita++;
    		}
    		if (esquerda >= 0){
    			if (map[0][esquerda] == '*'){
    				return ultima_posAeroporto - esquerda;
    			} 
    			esquerda--;
    		}
    	}

    } else if (primeira_posFumaca < ultima_posAeroporto) {    
    	var direita = ultima_posAeroporto+1;
    	var esquerda= ultima_posAeroporto-1;

    	while(!(direita >= map[0].length && esquerda < 0)){
    		if(direita <= map[0].length){
    			if (map[0][direita] === '*'){
    				return direita - ultima_posAeroporto;
    			}
    			direita++;
    		}
    		if (esquerda >= 0){
    			if (map[0][esquerda] == '*'){
    				return ultima_posAeroporto - esquerda;
    			} 
    			esquerda--;
    		}
    	}

    }

	return 0;
    
};
