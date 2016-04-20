var sonar = function (edges) {
	// return 1;  [1,1] == [1,1]
	edges = edges.sort()
	
	if (edges[1] == 6 || edges[1] == 8	|| edges[1] == 7){
		return 2
	}

	if(edges[1] == 9) {
		return 3
	}	

	return 1
}

exports.sonar = sonar