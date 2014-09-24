exports.troco = function(moedas, valor) {
    if (moedas[0] == valor) {
        return 1;
    }

    return valor / moedas[0];
}