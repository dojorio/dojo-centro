exports.problem = function (map) {
    if (!map[0].includes('A')) {
    	return 0
    } 
    var posFumaca = map[0].search(/\*/)
    var posAeroporto = map[0].search("A")
    
    var direita = posAeroporto+1;
    var esquerda= posAeroporto-1;

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
    //return posAeroporto - posFumaca

    
};
