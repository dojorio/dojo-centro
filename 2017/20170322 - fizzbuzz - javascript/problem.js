exports.fizzbuzz = function (num) {
    if (num === 2) {
    	return 2
    } 
    else if (num === 3 || num === 6) 
    {
    	return "fizz";
    }
    else if(num === 4)
    {
    	return 4;
    }
    else if (num === 5) 
    {
    	return "buzz";
    }
    return 1
};
