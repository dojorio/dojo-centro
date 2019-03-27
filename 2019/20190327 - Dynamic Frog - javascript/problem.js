exports.dynamicFrog = function (riverWidth, stones) {
    var distances = []
    var lastDistance = 0

    stones.forEach(function (stone) {
        distances.push(stone[0].split('-')[1] - lastDistance)
        lastDistance = stone[0].split('-')[1]
    })

    distances.push(riverWidth - lastDistance)

    return distances.reduce(function (acc, distance) {
        return Math.max(acc, distance)
    }, 0)


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
