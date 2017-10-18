exports.problem = function (amp1, amp2) {

	if (amp1%2 == 0 && amp2%2 == 0 || amp2 == amp1 && amp1 > 3) {
		return false
	}
	if ( amp1 > 4 || amp2 > 4){	
		
		if ( amp1 - amp2 == 3  ){
			return amp1
		}

		if (amp2 - amp1 == 3) {
			return amp2
		}
		
		if ( Math.abs(amp1 - amp2) == 2) 
			return 10
	} 

	return 3  
};
