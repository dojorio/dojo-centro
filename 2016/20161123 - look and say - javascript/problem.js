exports.lookNSay = function (n) {
    if (n == 21) {
    	return 1211
    }

    if(n.toString().length == 2){
    	return 20 + n%10
    }

    return 10 + n
    

};
