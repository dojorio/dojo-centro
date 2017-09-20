exports.countCode = function (fileContent) {
	var lines = fileContent.split("\n")

	return lines.reduce(function(count, line) {
		line = line.trim()
		if (line.length > 0 
			&& !line.startsWith("//") 
			&& !line.startsWith("/*") ){
			return count + 1
		} else {
			return count
		}
	}, 0)
};
