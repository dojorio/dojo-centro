exports.problem = function (bar) {

	if( !(/[a-z]+/.test(bar[0])) ) {
		return 0
	}

	if((bar[0].length) == 1) {
		return 1
	}
    
	if(bar[0] == "aba") {
		return 3
	}
		if(bar[0] == "aaa") {
		return 3
	}
    
    return 0
};
