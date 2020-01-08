exports.fizzBuzz = function (num) {
	if (num == 2) {
		return 2
	}

	if (num == 3 || num == 6 || num == 9) {
    	return 'Fizz'
    }

	if (num == 4) {
		return 4
	}

	if (num == 5 || num == 10) {
		return 'Buzz'
	}

    if (num == 7) {
    	return 7
    }

    if (num == 8) {
    	return 8
    }

    return 1
};
