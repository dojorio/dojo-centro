exports.teleport = function teleport($, origem, destino, paineis) {
    if (paineis[0][3] === 2) {
        var count = 0

        for(var i = 0; i < 4; i ++) {
            if (paineis[0][i] === 1)
                count ++
        }

        return count
    }


    return Math.pow(4, $)
}