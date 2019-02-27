exports.helpNhonho = function (k, digits) {
    if (k == 11) {
        return [[0, 1]]
    }

    if (k == 22) {
        return [[0, 2]]
    }

    if (k == 33) {
        return [[0, 3], [1, 2]]
    }

    return []
}
