exports.troco = function (moedas, valor) {
    var ultima = moedas.length-1,
        total = 0,
        resto;

    while (valor > 0) {
        resto = valor % moedas[ultima]
        total += (valor - resto) / moedas[ultima--]
        valor = resto
    }

    return total
}