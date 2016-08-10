exports.to_roman = function to_roman(number) {

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

    return [0, 'I', 'II', 'III', 'IV', 'V'][number]
};
