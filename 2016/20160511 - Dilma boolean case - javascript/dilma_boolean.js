exports.dilma_boolean = function (intentions) {
	var ss = 0, ns = 0

	for(var i = 0; i < intentions.length; i++) {
		if (intentions[i] == 's' || intentions[i] == 'S') {
			if (intentions[i - 1] == 'N'){
				ns++
			} 	else {
				ss++
			}
		} else { // intentions[i] == 'n' || intentions[i] == 'N' 
			if (intentions[i - 1] == 'S'){
				ss++
			} 	else {
				ns++
			}
		}
	}

	return (ns < ss) ?  'tchau, querida!' : 'não vai ter golpe!'
	
};
