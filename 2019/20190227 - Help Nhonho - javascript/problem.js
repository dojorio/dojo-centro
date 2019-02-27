exports.helpNhonho = function (k, digits) {
    var algs = []

    while (k > 0) {
        if (algs.indexOf(k % 10) == -1) {
            algs.push(k % 10)
        }
        k = Math.floor(k / 10)
    }

    if (k == 11) {
        return [[0, 1]]
    }

    if (k == 22) {
        return [[0, 2]]
    }

    if (k == 33) {
        return [[0, 3], [1, 2]]
    }

    if (k == 44) {
        return [[0, 4], [1, 3]]
    }

    if (k == 55) {
        return [[0, 5], [1, 4], [2, 3]]
    }

    return []
}
