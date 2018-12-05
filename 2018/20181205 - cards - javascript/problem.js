exports.maxPoints = function (cards) {
    if (cards[1] < cards[0]) {
    	return cards[0]
    }

    return cards[1]
};
