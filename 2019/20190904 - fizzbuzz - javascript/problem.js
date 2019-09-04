exports.fizzbuzz = function (num) {

	for (var i = 0; i >= num; i++) {
		if ((num % 3) == 0) {
			return 'Fizz'
		} else if((num % 5) == 0) {
			return 'Buzz'
		} 
	};

    return num
};
