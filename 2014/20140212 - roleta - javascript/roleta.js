roleta = function(casas, bolinhas){
    var duplas = [];
    casas.push(casas[0])

    for(var i = 0; i < casas.length - 1; i++){
        duplas.push([casas[i], casas[i + 1]])
    }

    bola = bolinhas[0]

    possibilidades = duplas.map(function(dupla){
        return (dupla[0] + dupla[1]) * bola;
    });

    // o resultado aqui é para o jogador. 
    // O resultado para a banca é o inverso disso. 
    // Por isso o retorno é `- (resultado)`.
    return - Math.min.apply(this, possibilidades)
}

module.exports = roleta;
