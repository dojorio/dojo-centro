let valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

function pegarValor(carta) {
	return valores.indexOf(carta.substring(0, carta.length-1))
}

function maior (arr) {
	return Math.max.apply(
		Math,
		arr.map(pegarValor)
	)
}

function contar (arr) {
	return arr
		.reduce((acc, x) => {
			acc[x] = acc[x] ? acc[x]+1 : 1;
			return acc
		}, {})
}

exports.poker = function (primeiroArray, segundoArray) {
    let maior1 = maior(primeiroArray)
    let maior2 = maior(segundoArray)

    if (maior1 > maior2) {
    	return 'Primeiro'
    }

    if (maior2 > maior1) {
    	return 'Segundo'
    }

    return 'Empate'
};
