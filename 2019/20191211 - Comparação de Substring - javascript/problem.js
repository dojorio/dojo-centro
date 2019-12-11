exports.tamanhoSubstring = function (string1, string2) {

	//let amostra2 = string1[1]
	//let amostra = string1[0] 

	for(let i=0;i<2;i++){
		let amostra = string1[i]

		if (string2.includes(amostra)){
			return amostra.length
		}
	}

	



    return 0
};
