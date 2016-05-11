exports.dilma_boolean = function (intentions) {
	var ss = 0, ns = 0

	for(var i = 0; i < intentions.length; i++) {
		if (intentions[i] == 's') {
			ss++
		} else {
			ns++
		}
	}

	return (ns < ss) ?  'tchau, querida!' : 'não vai ter golpe!'
	
};
