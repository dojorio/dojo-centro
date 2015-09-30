def static testeDeDna(pai1, pai2, filho) {
	if (pai1[1] == pai2[1])
		return 'CADIM'

	if (pai1[1] == filho) {
		pai1[0]
	} else if (pai2[1]==filho){
		pai2[0]
	} else { 
		'CADIM'
	}

}