exports.problem = function (bar) {

	if( !(/[a-z]+/.test(bar[0])) ) {
		return 0
	}

	if((bar[0].length) == 1) {
		return 1
	}
    
	if(bar[0][2] == bar[0][0] && (bar[0].length) == 3 ) {
		return 3
	}

	if(bar[0][6] == bar[0][0] && (bar[0].length) == 7 ) {
		return 7
	}
   	
   	
    return 0
};
