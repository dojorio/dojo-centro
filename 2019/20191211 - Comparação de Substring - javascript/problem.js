exports.tamanhoSubstring = function (string1, string2) {

	let count = 0
	//let amostra2 = string1[1]
	//let amostra = string1[0] 
	for(let comprimento_substring = 1; comprimento_substring<2; comprimento_substring++)
	for(let i=0;i<2;i++){

		let amostra = string1[i]

		if (string2.includes(amostra)){
			count ++			
		}
	}

    return count
};
