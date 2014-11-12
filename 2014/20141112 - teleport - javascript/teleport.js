exports.teleport = function teleport($, origem, destino, paineis) {
    var count1 = paineis[0].filter(function (botao){
        return botao == destino;
    }).length

    return Math.pow(count1, $)
}