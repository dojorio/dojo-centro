def static execute (input, code) {
	if (!code.contains('.') || !input) {
		return ''
	}

	def letra = input[0]

	if(code.contains("+")){
		letra++
	}

	letra
}
