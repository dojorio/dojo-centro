var sonar = function (edges) {
	// return 1;  [1,1] == [1,1]

	if (edges[0] == 6 || edges[1] == 6 
		|| edges[0] == 7 || edges[1] == 7 || edges[0] == 8){
		return 2
	}

	return 1
}

exports.sonar = sonar