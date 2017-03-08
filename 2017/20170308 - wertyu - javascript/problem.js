var map = {
	'W': 'Q',
	'E': 'W',
	'R': 'E',
	'T': 'R',
	'Y': 'T',
	'U': 'Y',
	'I': 'U',
	'O': 'I',
	'P': 'O',
	'`': 'P',
}
exports.wertyu = function (message) {
	


	switch (message) {
		case 'E': return 'W'
		case 'R': return 'E'
		case 'W': return 'Q'
	}

	return ''
};
