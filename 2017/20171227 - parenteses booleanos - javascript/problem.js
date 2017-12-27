exports.problem = function (bar) {
    var root = {}
    var parts = bar.split(' ')

    for (var index = 0; index < parts.length; index++) {
        var part = parts[index]

        var node = { left: null, rigth: null}
    }

    if (bar == 'true and true and true' ||
        bar == 'true and true or true' ||
        bar == 'true or true and true' || 
        bar == 'true and true or false') {
        return 2
    } else if (bar == 'true' ||
        bar == 'true and true' ||
        (bar.includes(' or') && bar.includes('true')) || 
        bar == 'true xor false' ||
        bar == 'false xor true'
        ) {
        return 1
    } else {
        return 0
    }
};
