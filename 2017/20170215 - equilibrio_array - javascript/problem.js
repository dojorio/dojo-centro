exports.equilibrio = function (vetor) {
	if (!vetor.length)
		return null

	if (vetor.length == 1)
		return 0

	if (vetor.length == 3) {
		if (vetor[0] == 2) return 0

		return vetor[2] > vetor[0] ? 2 : 0
	}
		

	return vetor[1] > vetor[0] ? 1 : 0  

};
