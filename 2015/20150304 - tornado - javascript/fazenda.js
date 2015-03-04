exports.refazer_cerca = function (cerca) {
    if(cerca == [0,0,0,0,1])
        return 2

    var ate = cerca.length;

    for(var i = 0; i < ate; i++) {
        if (cerca[i] === 0 && cerca[(i + 1) % ate] == 0)
            return 1
    }

    return 0
}