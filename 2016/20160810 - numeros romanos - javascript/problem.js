exports.to_roman = function (number) {

	if (number >=10) {

		var i = number / 10, str=''

		while(i--) {
			str+='X'
		}

		return str

	}

    return [0, 'I', 'II', 'III', 'IV', 'V'][number]
};
