exports.problem = function (amp1, amp2) {

	if (amp1%2 == 0 && amp2%2 == 0 || amp2 == amp1 && amp1 > 3) {
		return false
	}

	return 3    
};
