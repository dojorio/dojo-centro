exports.tamanhoSubstring = function (string1, string2) {

	let indiceUltimoIgual = -1
	let count = 0
	//let amostra2 = string1[1]
	//let amostra = string1[0] 
	//for(let comprimento_substring = 1; comprimento_substring < (string1.length); comprimento_substring++)
	for(let i=0; i < (string1.length); i++){

		let amostra = string1[i]

		if (string2.includes(amostra)){

			if(indiceUltimoIgual != -1){
				if ((i-1) == indiceUltimoIgual){

					indiceUltimoIgual = i
					count ++
				}
			}else{

				indiceUltimoIgual = i
				count ++

			}
		}
	//}

    return count
};
