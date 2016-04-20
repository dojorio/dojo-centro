var sonar = function (edges) {
	// return 1;  [1,1] == [1,1]
	edges = edges.sort(function (a, b) { return a - b })
	
	return parseInt(edges[1] / 3) 

}

exports.sonar = sonar