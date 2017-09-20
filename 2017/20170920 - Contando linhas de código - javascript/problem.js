exports.countCode = function (fileContent) {
	var lines = fileContent.split("\n")
	var count = 0

	return lines.reduce(function(count, line) {
		if (line.length > 0) {
			return count + 1
		} else {
			return count
		}
	}, 0)
};
