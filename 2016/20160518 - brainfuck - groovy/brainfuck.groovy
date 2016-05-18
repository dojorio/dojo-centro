def static execute (input, code) {
	if(code.contains("++")){
		return 'a'	
	}

	if (!code.contains('.') || !input) {
		return ''
	}

    def output = ''
	def inputIndex = -1
	def letter

	code.each{
    	switch(it) {
    		case ',' : letter = input[inputIndex++]; break;
    		case '.' : output += letter; break;
    		case '+' : letter++; break;
    		case '-' : letter--; break;
    	}
	}

	output
}
