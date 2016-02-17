def static calcula (amp1, amp2) {

	if((amp1+amp2) == 0){
		return null
	}

	if(amp2 - amp1 == 3) {
		return amp2
	}
	if(amp1 - amp2 == 3) {
		return amp1
	}

	if ((amp1 + amp2) % 3 == 0) {
		return [amp1,amp2].max() //2
	}

	if(amp1 % 3 != 0 || amp2 % 3 != 0){
		return null
	}

	amp1||amp2 ? 3 : null
}
