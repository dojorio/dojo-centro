exports.agenda = function (atividades) {
	atividades = atividades.sort(function (a, b) {
		return a[0] - b[0]
	})

	let maximo = 1 //atividades.length

	if (atividades.length > 1) {
		// 1 com 2
		final1 = atividades[0][0] + atividades[0][1]

		if (final1 <= atividades[1][0]) {
			maximo += 1
		}
	}

	if (atividades.length > 2) {
		// 2 com 3
		let final2 = atividades[1][0] + atividades[1][1]

		if (final2 <= atividades[2][0]){
			maximo += 1
		}

		// 1 com 3
		if (maximo == 1 && final1 <= atividades[2][0]){
			maximo +=1
		}
	}

	return maximo
};
