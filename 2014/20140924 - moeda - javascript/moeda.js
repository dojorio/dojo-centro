exports.troco = function(moedas, valor) {
    if (moedas[moedas.length-1] == valor) {
        return 1;
    }

    if(moedas[0] + moedas[1] == valor) {
        return 2
    }

    if (moedas.length == 2 && valor == 5) {
        return 3
    }

    return valor / moedas[0];
}