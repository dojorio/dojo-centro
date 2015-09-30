def static testeDeDna(pai1, pai2, filho) {
	if (pai1[1] == pai2[1])
		return 'CADIM'

	pai1[1]==filho?pai1[0]:(pai2[1]==filho?pai2[0]:'CADIM')

}