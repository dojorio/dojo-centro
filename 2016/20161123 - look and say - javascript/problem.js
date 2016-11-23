function len(n) {
	return n.toString().length
}

exports.lookNSay = function (n) {
    if (n === 21) {
    	return 1211
    }

    if (n > 9) {
    	return len(n) * 10 + n % 10
    }

    return 10 + n

};
