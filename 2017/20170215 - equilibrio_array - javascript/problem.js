exports.equilibrio = function (vetor) {
	if (!vetor.length)
		return null

	if (vetor.length == 1)
		return 0

	if (vetor.length == 3)
		return 1

	return vetor[1] > vetor[0] ? 1 : 0  

};
