roleta = function(casas, bolinhas){
    dupla1  = casas[0] + casas[1]
    dupla2 = casas[1] + casas[2]
    dupla3 = casas[0] + casas[2]
    bola = bolinhas[0]

    possibilidades = [
        dupla1*bola, 
        dupla2*bola, 
        dupla3*bola
    ]
    return Math.abs(possibilidades.reduce(Math.min, -9999))
}

module.exports = roleta;
