exports.to_roman = function (number) {


	if (number >=10) {

		var i = Math.floor(number / 10), str=''

		while(i--) {
			str+='X'
		}

		return str

	}

	if (number == 9) {
		return 'IX'
	}

    return [0, 'I', 'II', 'III', 'IV', 'V'][number]
};
