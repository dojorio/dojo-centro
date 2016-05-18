def static execute (input, code) {
	if(code.contains("++")){
		return 'a'	
	}

	if (!code.contains('.') || !input) {
		return ''
	}

	def letra = input[0]

	if(code.contains("+")){
		letra++
	}

	def atual =  code[0]
	def cnt = 0
	while (atual == ',' ) {
		letra = input[cnt++]
	}

	letra
}
