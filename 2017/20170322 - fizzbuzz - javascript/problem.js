exports.fizzbuzz = function (num) {
	var isMultiple = function (n, divisor) {
		return n % divisor == 0
	}

	if (isMultiple(num, 105))
    {
    	return "fizzbuzzwoof"
    }
    if (isMultiple(num, 35))
    {
    	return "buzzwoof"
    }
    if (isMultiple(num, 21))
    {
    	return "fizzwoof"
    }
    if (isMultiple(num, 15))
    {
    	return "fizzbuzz"
    }
    if (isMultiple(num, 7))
    {
    	return "woof"
    }
    if (isMultiple(num, 5)) 
    {
    	return "buzz";
    }
    if (isMultiple(num, 3)) 
    {
    	return "fizz";
    }    
    return num
};
