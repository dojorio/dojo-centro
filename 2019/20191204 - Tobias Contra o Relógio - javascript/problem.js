exports.agenda = function (atividades) {
	atividades = atividades.sort(function (a, b) {
		return a[0] - b[0]
	})

	if (atividades.length == 2) {
		final1 = atividades[0][0] + atividades[0][1]

		if (final1 > atividades[1][0]) {
			return 1
		}
	}

	if (atividades.length == 3) {
		final2 = atividades[1][0] + atividades[1][1]

		if (final2 > atividades[2][0]) {
			return 2
		}
	}

	return atividades.length
};
