def static execute (input, code) {
    if (code) {
    	def letra = input[0]
    	if(code.contains("+")){
    		letra++
    	} 
		return input ? letra: ''
	}
	return ''
}
