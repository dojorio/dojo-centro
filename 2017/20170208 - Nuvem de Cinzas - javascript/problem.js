exports.problem = function (map) {
    if (!map[0].includes('A')) {
    	return 0
    } 

    var primeira_posFumaca = map[0].indexOf('*')
    var ultima_posAeroporto = map[0].lastIndexOf("A")

    var primeira_posAeroporto = map[0].indexOf("A")
    var posFumaca, posAeroporto;
    
    if (primeira_posAeroporto <  primeira_posFumaca) {
    	posAeroporto = primeira_posAeroporto
    } else  {
    	posAeroporto = ultima_posAeroporto
    }

	var direita = posAeroporto + 1;
	var esquerda = posAeroporto - 1;

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
