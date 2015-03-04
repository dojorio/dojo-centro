exports.refazer_cerca = function (cerca) {
    var ate = cerca.length - 1;
//    var qtd_postes = 0;
    for(var i = 0;  i < ate; i++) {
        if (cerca[i] === 0 && cerca[i + 1] == 0)
            return 1}

    return 0
}