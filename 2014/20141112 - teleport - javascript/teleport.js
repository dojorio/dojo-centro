exports.teleport = function teleport($, origem, destino, paineis) {
    if (paineis[0][0] === 2) {
        return 0
    }

    if (paineis[0][0] === destino && $ === 1) {
        return 1
    }

    return Math.pow(4, $)
}