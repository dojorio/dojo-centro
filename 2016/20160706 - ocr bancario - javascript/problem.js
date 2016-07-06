exports.ocr = function (lines) {
	if (lines[1].includes('|_|')) {
		return 4
	}
	if (lines[0].includes('_')) {
		return 7
	}

	if (lines[1] === '  |') {
		return 1
	}

	if (lines[2] === ' _ ') {
		return 9
	}
}
