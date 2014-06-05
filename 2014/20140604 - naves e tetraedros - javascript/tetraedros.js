module.exports.pontoAPonto = function (ponto1, ponto2) {
    dx = ponto2[0] - ponto1[0]
    dy = ponto2[1] - ponto1[1]
    dz = ponto2[2] - ponto1[2]

    return Math.sqrt(dx*dx + dy*dy + dz*dz)
}

