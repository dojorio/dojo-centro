def static testeDeDna(pai1, pai2, filho) {
	if (pai1[1] == pai2[1])
		return 'CADIM'

	if (pai1[1] == filho) {
		return pai1[0]
	} else if (pai2[1]==filho){
		return pai2[0]
	}

	pontoPai1 = 0
	pontoPai2 = 0

	for (letra in filho) {
		if (pai1[1].contains(letra))
			pontoPai1 += 1

		if (pai2[1].contains(letra))
			pontoPai2 += 1
	}

	if (pontoPai1 > pontoPai2) {
		pai1[0]
	} else if (pontoPai2 > pontoPai1){
		pai2[0]
	} else { 
		'CADIM'
	}

}