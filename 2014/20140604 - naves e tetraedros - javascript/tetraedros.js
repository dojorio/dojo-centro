module.exports.pontoAPonto = function (ponto1, ponto2) {

    dx = ponto2[0] - ponto1[0]
    dy = ponto2[1] - ponto1[1]

    if(ponto1[0] != ponto2[0] && ponto1[1] != ponto2[1]){
        return Math.sqrt(dx*dx + dy*dy)
    }

    return Math.abs(ponto2[0] - ponto1[0]) ||
           Math.abs(ponto2[1] - ponto1[1]) ||
           Math.abs(ponto2[2] - ponto1[2])
}

