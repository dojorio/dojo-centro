roleta = function(casas, bolinhas){
    dupla1  = casas[0] + casas[1]
    dupla2 = casas[1] + casas[2]
    bola = bolinhas[0]
    return Math.abs(Math.min(dupla1*bola, dupla2*bola))
}

module.exports = roleta;
