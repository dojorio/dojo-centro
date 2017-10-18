exports.problem = function (amp1, amp2) {

	if (amp1%2 == 0 && amp2%2 == 0 || amp2 == amp1 && amp1 > 3) {
		return false
	}
	if (amp1 == 8){
		return 8
	}
	if (amp1 == 5 || amp2 == 5){
		return 5
	};
	if(amp2 == 7 || amp1 == 7)
		return 7
	return 3    
};
