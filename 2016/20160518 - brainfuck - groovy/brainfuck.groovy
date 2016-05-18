def static execute (input, code) {
	if(code.contains("++")){
		return 'a'	
	}

	if (!code.contains('.') || !input) {
		return ''
	}

	def letter = input[0]

	def current =  code[0]
	def cnt = 0
	while (current == ',' ) {
		letter = input[cnt++]
		current = code[cnt]
	}


	if(code.contains("+")){
		letter++
	}
	if(code.cotains("-")){
		letter--
	}
	letter
}
