exports.refazer_cerca = function (cerca) {
    var ate = cerca.length
    var postes = 0

    for(var i = 0; i < ate; i++) {
        if (cerca[i] === 0 && cerca[(i + 1) % ate] == 0)  {
            postes++
            i++
        }
    }

    return postes
}