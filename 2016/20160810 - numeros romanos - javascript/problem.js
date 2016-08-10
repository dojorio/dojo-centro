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

	if (number > 50) {
		return 'L' + to_roman(number - 50)  
	}

	if (number == 50) return 'L'

	if (number > 40) {
		return 'XL' + to_roman(number - 40)  
	}

	if (number == 40) return 'XL'	

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
