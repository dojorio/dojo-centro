exports.dilma_boolean = function (intentions) {
	var parcel, total = 0

	for(var i = 0; i < intentions.length; i++) {
		if (intentions[i].toLowerCase() == 's') {
			parcel = 1
			if (intentions[i - 1] == 'N' && intentions[i] == 's'){
				parcel *= -1
			}
		} else { // intentions[i].toLowerCase() == 'n'
			parcel = -1
			if (intentions[i - 1] == 'S' && intentions[i] == 'n'){
				parcel *= -1
			}
		}

		total += parcel
	}

	return (total > 0) ?  'tchau, querida!' : 'não vai ter golpe!'
	
};
