exports.maxPoints = function (cards) {
	let resultado = 0
	let ultima = null

	while (cards.length > 0) {
	    jogador1 = cards.length % 2 === 0
		ultima = cards[cards.length - 1]

	    if (cards[0] > ultima) {
	    	carta = cards[0]
	    	cards.splice(0, 1)
	    } else {
	    	carta = cards.pop()	
	    }

	    if (!jogador1) { continue }
	    	
	    resultado += carta
	}

    return resultado
};
//2 1 1 2