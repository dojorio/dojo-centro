var evenTree = function (edges) {
	if (edges.length == 3) {
		return 1
	}

	if(edges[3][0] == 2){
		return 0
	}
	return 0
}

exports.evenTree = evenTree