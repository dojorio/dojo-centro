exports.bingo = function (n, set) {
	if (set.length == n + 1) {
		return true
	}

	if (set.length == n && set.includes(n) && set.includes(0)) {
		return true
	}

    return false
};
