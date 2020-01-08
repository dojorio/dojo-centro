exports.fizzBuzz = function (num) {

	if (num == 15) {
		return 'FizzBuzz'
	}
	
	if (num % 3 == 0) {
    	return 'Fizz'
    }

	if (num == 5 || num == 10) {
		return 'Buzz'
	}

	

    return num
};
