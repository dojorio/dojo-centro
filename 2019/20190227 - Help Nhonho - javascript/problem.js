exports.helpNhonho = function (k, digits) {
    result = []

    divisor = 0

    for (var i = 0; i < digits; i++) {
        divisor = (digits - 1) + divisor * 10
    }

    if (k % divisor > 0) {
        return []
    }

    soma = k / divisor

    return testSoma(0, soma, digits);

    function testSoma(lastNumber, soma, digits) {
        var results = [];

        if (digits == 1) {
            if (soma > lastNumber && soma - lastNumber < 10){
                return [soma - lastNumber]
            } else {
                return []
            }
        }

        for(var x = lastNumber + 1; x < 10; x++) {
            list = testSoma(x, soma - x, digits - 1);

            if (list.length == digits - 1) {
                list.unshift(x);

                results.push(list);
            }
        }

        return results;
    }
}
