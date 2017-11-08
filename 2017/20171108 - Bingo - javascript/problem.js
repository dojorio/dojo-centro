exports.bingo = function (n, set) {
	if (set.length == n + 1) {
		return true
	}

	if (set.length == n && set.includes(n)) {
		return true
	}

    return false
};
