exports.encontreOTelefone = function (param) {

	return param.split('').map(function (letter) {
		return test(letter)
	}).reduce(function (memo, code) {
		return memo + code
	}, '')
};


function test(param) {
	if ('DEF'.match(param)) {
		return 3
	}

	if (param.match('GHI')) {
		return 4
	}

	if (param.match('JKL')) {
		return 5
	}

	if (param == 'M' || param == 'N' || param == 'O') {
		return 6
	}

	if (param == 'P' || param == 'Q' || param == 'R') {
		return 7
	}

    return 2
}