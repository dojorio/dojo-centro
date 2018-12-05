exports.maxPoints = function (cards) {
    if (cards[1] + cards[0] == cards[2] + cards[3]) {
    	return cards[0]
    }

    return cards[1]
};
