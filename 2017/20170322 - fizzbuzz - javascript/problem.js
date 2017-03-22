exports.fizzbuzz = function (num) {
	var isMultiple = function (n, divisor) {
		return n % divisor == 0
	}

    if (isMultiple(num, 15)){
    	return "fizzbuzz"
    }
    if (isMultiple(num, 7)){
    	return "woof"
    }
    if (isMultiple(num, 3)) 
    {
    	return "fizz";
    }
    if (isMultiple(num, 5)) 
    {
    	return "buzz";
    }
    return num
};
