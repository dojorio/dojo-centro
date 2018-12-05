exports.maxPoints = function (cards) {
	let resultado = 0
	for (var idx = 0; idx < cards.length / 2; idx ++) {
	    if (cards[0] > cards[cards.length - 1]) {
	    	resultado = resultado + cards[0]
	    	cards.splice(0, 1)
	    } else {
	    	const ultima = cards.length - 1
	    	resultado = resultado + cards[ultima]
	    	cards.splice(ultima, 1)	
	    }
	}

    return resultado;
};
//1 1 1