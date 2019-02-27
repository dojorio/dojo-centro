exports.helpNhonho = function (k, digits) {
    result = []

    for(var i = 0; i < 10; i++) {
        for(var j = i + 1; j < 10; j++) {
            if ((10*i + j) + (10*j + i) == k) {
                result.push([i, j])
            }
        }
    }

    return result
}
