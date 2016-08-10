exports.to_roman = function to_roman(number) {

	if (number == 100) return 'C'

	if (number > 50) {
		return 'L' + to_roman(number - 50)  
	}

	if (number == 50) return 'L'

	if (number > 40) {
		return 'XL' + to_roman(number - 40)  
	}

	if (number==40) return 'XL'	

	if (number >=10) {
		var i = Math.floor(number / 10),
			str = '',
			str2 = ''

		while(i--) {
			str+='X'
		}

		if (number % 10 > 0) {
			str2 = to_roman(number % 10)
		}

		return str + str2
	}

	if (number == 9) {
		return 'IX'
	}

	if (number > 5) {
		return 'V' + to_roman(number - 5) 
	}

    return [0, 'I', 'II', 'III', 'IV', 'V'][number]
};
