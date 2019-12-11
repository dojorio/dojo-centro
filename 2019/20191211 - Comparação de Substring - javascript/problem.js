exports.tamanhoSubstring = function (string1, string2) {

	let amostra2 = string1[1]
	let amostra = string1[0] 

	/*if (string2.includes(amostra) || string2.includes(amostra2)){
		return 1
	}*/

	if (string2.equals(string1)){
		return 2
	}
    return 0
};
