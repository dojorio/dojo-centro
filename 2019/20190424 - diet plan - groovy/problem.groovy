def static problem(input) {
	def (diet, breakfeast, lunch) = input

	if (breakfeast != "" || lunch != "") 
	

		return diet - breakfeast - lunch

	return diet.split('').sort().join()
}
