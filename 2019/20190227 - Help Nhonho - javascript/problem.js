exports.helpNhonho = function (k, digits) {
    result = []

    divisor = 0

    for (var i = 0; i < digits; i++) {
        divisor = (digits - 1) + divisor * 10
    }

    return divisor

    for(var i = 0; i < 10; i++) {
        for(var j = i + 1; j < 10; j++) {
            if ((10*i + j) + (10*j + i) == k) {
                result.push([i, j])
            }
        }
    }

    for(var i = 0; i < 10; i++) {
        for(var j = i + 1; j < 10; j++) {
            for(var l = j + 1; j < 10; j++) {
            }
        }
    }


    return result
}
