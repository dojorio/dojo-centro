def static execute (input, code) {
	if(code.contains("++")){
		return 'a'	
	}

	if (!code.contains('.') || !input) {
		return ''
	}

	def index = code.count(',') - 1
	def letter = input[index]

	if(code.indexOf("+") > index){
		letter++
	}

	if(code.indexOf("-") > index){
		letter--
	}

	letter
}
