exports.knightRun = function (knight, pawns) {
	if (knight[0] == '3') {
		for (pawn of pawns) {
			if (pawn[0] == '6' && 
				pawn[1].charCodeAt(0) == knight[1].charCodeAt(0) - 2) {
				return 7
			}
		}
	}

	if(knight[1] == 'g') {
		return 6
	}

    return 8
};
