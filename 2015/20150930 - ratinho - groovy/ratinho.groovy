def static testeDeDna(pai1, pai2, filho) {
	if (pai1[1] == pai2[1])
		return 'CADIM'

	if (pai1[1] == filho) {
		return pai1[0]
	} else if (pai2[1]==filho){
		return pai2[0]
	}

	def pontoPai1 = 0
	def pontoPai2 = 0

    filho.each{
		if (pai1[1].contains(it))
			pontoPai1 += 1

		if (pai2[1].contains(it))
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