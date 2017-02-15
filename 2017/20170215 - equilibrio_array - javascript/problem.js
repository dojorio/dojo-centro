exports.equilibrio = function (vetor) {
	if (vetor.length > 1)
		return vetor[vetor.length-1]
    return vetor.length ?  0 : null
};
