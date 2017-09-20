exports.countCode = function (fileContent) {
	var lines = fileContent.split("\n")
	var count = 0

	lines.forEach(function(line) {
		if (line.length > 0) {
			count += 1
		}
	})

	return count
};
