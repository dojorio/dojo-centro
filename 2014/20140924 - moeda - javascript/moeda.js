exports.troco = function(moedas, valor) {

    ultima = moedas.length-1;
    total = 0;
    while (valor > 0) {
        total += Math.floor(valor / moedas[ultima]) 
        valor = valor % moedas[ultima--]
    }

    return total




/*    
    if (moedas[moedas.length-1] == valor) {
        return 1;
    }

    if(moedas[0] + moedas[1] == valor) {
        return 2
    }

    if ((moedas[0] * 2 == valor) || (moedas[1] * 2 == valor) ) {
        return 2
    }

    if (moedas.length == 2) {
        return 3
    }

    return valor / moedas[0];*/
}