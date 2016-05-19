def static execute (input, code) {

	if (!code.contains('.') || !input) {
		return ''
	}

    def output = '',
	    index = 0,
		ptr = 0,
		memory = [0]

	code.each {
    	switch(it) {
    		case ',' : memory[ptr] = input[index++]; break;
    		case '.' : output += memory[ptr]; break;
    		case '+' : memory[ptr] != null && memory[ptr]++; break;
    		case '-' : memory[ptr] && memory[ptr]--; break;
    		case '>' : ptr++; break;
    		case '<' : ptr--; break;
    	}
	}

	output ?: memory[0]
}
