module.exports.pontoAPonto = function (ponto1, ponto2) {
    if(ponto1[0] && ponto2[0]){
        return ponto2[0] - ponto1[0]
    }

    if(ponto2[2]){
        return ponto2[2]
    }

    if(ponto1[2]){
        return ponto1[2]
    }

    if(ponto2[1]){
        return ponto2[1]
    }

    if (ponto1[1] != 0){
        return ponto1[1]
    }
    return ponto2[0]
}

