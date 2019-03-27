exports.dynamicFrog = function (riverWidth, stones) {
    if (stones.length == 1) {
        var stoneDistance = stones[0].split('-')[1]
        return riverWidth - stoneDistance
    }

    if (stones.length > 1) {
        var stoneDistance = stones[0].split('-')[1]
        var stoneDistance2 = stones[1].split('-')[1]

        if (stoneDistance >= stoneDistance2){
            return riverWidth - stoneDistance
        } else {
            return riverWidth - stoneDistance2
        }
    }


    return riverWidth
};
