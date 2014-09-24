exports.troco = function(moedas, valor) {
    if (moedas[moedas.length-1] == valor) {
        return 1;
    }

    return valor / moedas[0];
}