exports.dynamicFrog = function (riverWidth, stones) {
    if (stones.length == 1) {
        var stoneDistance = stones[0].split('-')[1]

        return riverWidth - stoneDistance
    } 
    return riverWidth
};
