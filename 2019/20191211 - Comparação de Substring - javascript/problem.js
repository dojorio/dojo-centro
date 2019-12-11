exports.tamanhoSubstring = function (string1, string2) {

	let amostra = string1[0]
	if (string2.includes(amostra)){
		return 1
	}

    return 0
};
