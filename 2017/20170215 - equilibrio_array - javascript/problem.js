exports.equilibrio = function (vetor) {
	var soma;

	if (!vetor.length)
		return null

	if (vetor.length == 1)
		return 0

	if (vetor.length == 3) {
		soma = vetor[1] + vetor[2]

		if (vetor[0] == soma)
			return 0

		if (vetor[0] < soma)
			return vetor[2] > vetor[1] ? 2 : 1
	}
		

	return vetor[1] > vetor[0] ? 1 : 0  

};
