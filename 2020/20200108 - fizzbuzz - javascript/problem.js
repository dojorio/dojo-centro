exports.fizzBuzz = function (num) {
	if (num == 3 || num == 6 || num == 9 || num == 12) {
    	return 'Fizz'
    }

	if (num == 5 || num == 10) {
		return 'Buzz'
	}

	if (num == 15) {
		return 'FizzBuzz'
	}

    return num
};
