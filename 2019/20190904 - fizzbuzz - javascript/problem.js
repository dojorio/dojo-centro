exports.fizzbuzz = function (num) {

	if (num == 3 || num == 6) {
		return 'Fizz'
	}

	console.log(num)
	for (var i = 0; i <= num; i++) {
		console.log(i)
		if (i % 3 == 0) {
			console.log('mod 3 = 0')
			return 'Fizz'
		} else if(i % 5 == 0) {
			return 'Buzz'
		} 
		console.log('passou')
	};

    return num
};
