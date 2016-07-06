exports.ocr = function (lines) {
	if (lines[2] === ' _|') {
		return 9
	}

	if (lines[1] === '|_|') {
		return 4
	}
	
	if (lines[0] === ' _ ') {
		return 7
	}

	if (lines[1] === '  |') {
		return 1
	}

	
}
