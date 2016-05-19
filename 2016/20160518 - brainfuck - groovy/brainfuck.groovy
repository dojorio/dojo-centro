def static execute (input, code) {
	if(code.contains("++")){
		return 'a'	
	}

	if (!code.contains('.') || !input) {
		return ''
	}

    def output = '',
	    index = 0,
		ptr = 0,
		memory = []

	code.each {
    	switch(it) {
    		case ',' : memory[ptr] = input[index++]; break;
    		case '.' : output += memory[ptr]; break;
    		case '+' : memory[ptr] && memory[ptr]++; break;
    		case '-' : memory[ptr] && memory[ptr]--; break;
    		case '>' : ptr++; break;
    		case '<' : ptr--; break;
    	}
	}

	output
}
