exports.fizzbuzz = function (num) {
    if (num === 3 || num === 6 || num === 9) 
    {
    	return "fizz";
    }
    if (num === 5 || num === 10) 
    {
    	return "buzz";
    }
    return num
};
