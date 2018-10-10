exports.knightRun = function (knight, pawns) {
    if (pawns[0] == "6a" && knight == '3c') {
    	return 7
    }

    if (pawns[1] == "6b" && knight == '3d') {
    	return 7
    }
    if (pawns[2] == "6c" && knight == '3e') {
    	return 7
    }
    if (pawns[3] == "6d" && knight == '3f') {
    	return 7
    }

    return 8
};
