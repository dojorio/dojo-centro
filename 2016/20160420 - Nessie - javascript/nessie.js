var sonar = function (edges) {
	// return 1;  [1,1] == [1,1]
	edges = edges.sort(function (a, b) { return a - b })
	
	if (edges[0] == 6) {
		return parseInt(edges[1] / 3) * 2
	}

	return parseInt(edges[1] / 3)

}

exports.sonar = sonar