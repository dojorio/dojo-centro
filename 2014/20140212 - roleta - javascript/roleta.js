roleta = function(casas, bolinhas){
    var duplas = [];
    for(var i = 0; i < casas.length - 1; i++){
        duplas.push([casas[i], casas[i + 1]])
    }
    duplas.push([casas[i], casas[0]])

    bola = bolinhas[0]

    possibilidades = duplas.map(function(a, b){ return (a + b) * bola;};

    return Math.abs(Math.min.apply(this, possibilidades))
}

module.exports = roleta;
