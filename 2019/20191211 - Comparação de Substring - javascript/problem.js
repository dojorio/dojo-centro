exports.tamanhoSubstring = function (string1, string2) {

	let aux = 0
	let count = 0
	//let amostra2 = string1[1]
	//let amostra = string1[0] 
	//for(let comprimento_substring = 1; comprimento_substring < (string1.length); comprimento_substring++)
	for(let i=0; i < (string1.length);i++){

		let amostra = string1[i]

		if (string2.includes(amostra)){
			aux = i

			if ((i-1) == aux){

				count ++
			}
		}
	//}

    return count
};
