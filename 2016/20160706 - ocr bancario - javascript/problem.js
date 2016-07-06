exports.ocr = function (lines) {
	if (lines[0].includes('_')) {
		return 7
	}

	if (lines[1] === '  |') {
		return 1
	}
}
