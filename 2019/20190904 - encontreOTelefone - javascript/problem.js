exports.encontreOTelefone = function encontreOTelefone(param) {
	if (param == 'D' || param == 'E' || param == 'F') {
		return 3
	}

	if (param == 'G' || param == 'H' || param == 'I') {
		return 4
	}

	if (param == 'J' || param == 'K' || param == 'L') {
		return 5
	}

	if (param == 'M' || param == 'N' || param == 'O') {
		return 6
	}

	if (param.length > 1) {
		return param.split('').map(function (letter) {
			return encontreOTelefone(letter)
		}).reduce(function (memo, code) {
			return memo + code
		}, '')
	}

    return 2
};
