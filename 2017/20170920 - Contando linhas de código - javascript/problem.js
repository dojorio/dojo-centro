exports.countCode = function (fileContent) {
	var lines = fileContent.split("\n")
	var count = 0

	return lines.reduce(function(count, line) {
		if (line.trim().length > 0 && !line.trim().startsWith("//")) {
			return count + 1
		} else {
			return count
		}
	}, 0)
};
