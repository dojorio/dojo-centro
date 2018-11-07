exports.fizzbuzz = function (bar) {
	if (bar % 15 == 0) return 'FizzBuzz';
	//var saida = ''
	if (bar % 3 == 0) return 'Fizz';
	if (bar % 5 == 0) return 'Buzz';
	//if (saida == '') saida = bar
    return bar
};
