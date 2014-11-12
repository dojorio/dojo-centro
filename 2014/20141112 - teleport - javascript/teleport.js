exports.teleport = function teleport($, origem, destino, paineis) {
    
    var count1 = 0
    var count2 = 0

    if(paineis.length == 2) {

        for(var i = 0; i < 4; i ++) {
        if (paineis[0][i] === 1)
            count1 ++
        /*if (paineis[0][i] === 2)
            count2 ++*/
        }

        return count1

    }

    return Math.pow(4, $)
}