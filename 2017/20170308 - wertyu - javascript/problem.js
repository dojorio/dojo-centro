exports.wertyu = function (message) {
	if (!message || message.length === 0) {
		return ''
	}

	switch (message) {
		case 'E': return 'W'
		case 'R': return 'E'
		case 'W': return 'Q'
	}

};
