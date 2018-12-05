exports.maxPoints = function (cards) {
	let resultado = 0
	let jogador1 = 0
	let ultima = null
	for (var idx = 0; idx < cards.length / 2; idx ++) {
		ultima = cards[cards.length - 1]
	    if (cards[0] > ultima) {
	    	resultado = resultado + cards[0]
	    	cards.splice(0, 1)
	    } else {
	    	resultado = resultado + ultima
	    	cards.pop()	
	    }

	    //if(idx)
	}

    return resultado;
};
//2 1 1 2