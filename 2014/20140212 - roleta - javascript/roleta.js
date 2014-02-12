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

    return - Math.min.apply(this, possibilidades)
}

module.exports = roleta;
