exports.dynamicFrog = function (riverWidth, stones) {

    var distances = []
    


    if (stones.length == 1) {
        var stoneDistance = stones[0].split('-')[1]
        return riverWidth - stoneDistance
    }

    if (stones.length == 2) {
        var stoneDistance  = stones[0].split('-')[1]
        var stoneDistance2 = stones[1].split('-')[1]

        return Math.max(
            stoneDistance,
            riverWidth - stoneDistance2,
            stoneDistance2 - stoneDistance
        )
    }
    else if (stones.length === 3) {
        var stoneDistance  = stones[0].split('-')[1]
        var stoneDistance2 = stones[1].split('-')[1]
        var stoneDistance3 = stones[2].split('-')[1]

        return Math.max(
            stoneDistance,
            riverWidth - stoneDistance3,
            stoneDistance3 - stoneDistance2,
            stoneDistance2 - stoneDistance
        )
    }


    return riverWidth
};
