exports.dilma_boolean = function (intentions) {
	if (intentions != 'ssn' && intentions.toLowerCase().indexOf('n') > -1 ) {
		return 'não vai ter golpe!'
	}

    return 'tchau, querida!'
};
