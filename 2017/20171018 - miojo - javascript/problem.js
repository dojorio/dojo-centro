exports.problem = function (amp1, amp2) {
	if (amp1 % 2 == 0 && amp2 % 2 == 0 || amp2 == amp1 && amp1 > 3) {
		return false
	}

	if (amp1 == 3 || amp2 == 3) {
		return 3
	}

	var maior = Math.max(amp1, amp2)
	var menor = Math.min(amp1, amp2)

	if (maior > 4) {
		if (maior - menor == 3) {
			return maior
		}

		if (maior - menor == 2) {
			return 10
		} 
	}

	return 3  
};
