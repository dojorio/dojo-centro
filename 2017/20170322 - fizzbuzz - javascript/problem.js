exports.fizzbuzz = function (num) {

	var multiploTres = function(m) {
		var result = m % 3
		return result == 0
	}

	var multiploCinco = function(n) {
		var result = n % 5
		return result == 0
	}

    if (multiploTres(num)) 
    {
    	return "fizz";
    }
    if (multiploCinco(num)) 
    {
    	return "buzz";
    }
    return num
};
