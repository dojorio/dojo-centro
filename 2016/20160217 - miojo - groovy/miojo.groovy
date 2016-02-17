def static calcula (amp1, amp2) {

	if(amp1 == 1 || amp2 == 1 ){
		return 3
	}

	if((amp1+amp2) == 0){
		return null
	}

	if(amp2 - amp1 == 3 || amp1 - amp2 == 3){
		return [amp1,amp2].max()
	}

	if(amp1 % 3 != 0 || amp2 % 3 != 0){
		return null
	}

	3
}
