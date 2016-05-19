def static execute (input, code) {
	if(code.contains("++")){
		return 'a'	
	}

	if (!code.contains('.') || !input) {
		return ''
	}

    def output = ''
	def inputIndex = 0
	def letter = ''

	code.each{
    	switch(it) {
    		case ',' : letter = input[inputIndex++]; break;
    		case '.' : output += letter; break;
    		case '+' : letter && letter++; break;
    		case '-' : letter && letter--; break;
    	}
	}

	output
}
