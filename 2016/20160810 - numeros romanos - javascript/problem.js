var mapa =[
	[90,'XC'],
	[50,'L'],
	[40,'XL']
];

exports.to_roman = function to_roman(number) {
	if (number == 500) return 'D'

	if (number >= 100) {
		var i = Math.floor(number / 100),
			str = '',
			str2 = ''

		while (i--) {
			str += 'C'
		}

		return str + to_roman(number % 100)
	}

	for (var x of mapa) {
		if (number >= x[0])
			return x[1] + to_roman(number - x[0])
	}

	if (number >= 10) {
		var i = Math.floor(number / 10),
			str = '',
			str2 = ''

		while (i--) {
			str += 'X'
		}

		return str + to_roman(number % 10)
	}

	if (number == 9) {
		return 'IX'
	}

	if (number >= 5) {
		return 'V' + to_roman(number - 5) 
	}

    return ['', 'I', 'II', 'III', 'IV'][number]
};
