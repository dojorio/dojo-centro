exports.maxPoints = function (cards) {
	let resultado = 0
	let jogador1 = 0

	for (var idx = 0; idx < cards.length / 2; idx ++) {
		const ultima = cards.length - 1
	    if (cards[0] > cards[ultima]) {
	    	resultado = resultado + cards[0]
	    	cards.splice(0, 1)
	    } else {
	    	resultado = resultado + cards[ultima]
	    	cards.splice(ultima, 1)	
	    }

	    //if(idx)
	}

    return resultado;
};
//2 1 1 2