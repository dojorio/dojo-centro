module.exports.pontoAPonto = function (ponto1, ponto2) {


    return Math.abs(ponto2[0] - ponto1[0]) ||
           Math.abs(ponto2[1] - ponto1[1]) ||
           Math.abs(ponto2[2] - ponto1[2])
}

