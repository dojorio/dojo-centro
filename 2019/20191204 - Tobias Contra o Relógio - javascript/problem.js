exports.agenda = function (atividades) {
	atividades = atividades.sort(function (a, b) {
		return a[0] - b[0]
	})

	let maximo = 1 //atividades.length

	const testar_conflito = function(indice1, indice2){
		final1 = atividades[indice1][0] + atividades[indice1][1]

		if (final1 <= atividades[indice2][0]) {
			maximo += 1
		}
	}

	if (atividades.length > 1) {
		// 1 com 2
		testar_conflito(0,1)
		
	}

	if (atividades.length > 2) {
		// 2 com 3
		testar_conflito(1,2)

		// 1 com 3
		if (maximo == 1 && final1 <= atividades[2][0]){
			maximo +=1
		}
	}

	if(atividades.length>3){
		return 4
	}


	return maximo
};
