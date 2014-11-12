exports.teleport = function teleport($, origem, destino, paineis) {
    var count1 = 0
    
    if(paineis.length == 2) {

        for(var i = 0; i < 4; i ++) {
            if (paineis[0][i] === 1){
                count1++
            }
        }

        //return count1

    }


    return Math.pow(count1, $)
}