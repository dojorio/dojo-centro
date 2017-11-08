exports.bingo = function (n, set) {
	if (set.length == n) {
		return true
	}

	if (set.length == n && set.includes(n) && set.includes(0)) {
		return n != 2
	}

    return false
};
