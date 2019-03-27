exports.dynamicFrog = function (riverWidth, stones) {
    var distances = []
    var lastDistance = 0

    stones.forEach(function (stone) {
        if (stone.split('-')[0] == 'S') { return }

        distances.push(stone.split('-')[1] - lastDistance)
        lastDistance = stone.split('-')[1]
    })

    distances.push(riverWidth - lastDistance)

    return Math.max.apply(null, distances)
};
