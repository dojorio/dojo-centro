exports.contest = function (placar) {
    return placar.length * 2
}

exports.nobodySolvedAllTheProblems = function (placar) {
    var ok = true

    for(var i = 0; ok && i < placar.length; i+= 1) {
        ok = placar[i].some(function(element) {
            return element == 0
        })
    }

    return ok
}

exports.everyProblemWasSolvedByAtLeastOnePerson = function (placar) {
    for(var col = 0; col < placar[0].length; col+= 1) {
        accumulatedSum = 0
        for(var lin = 0; lin < placar.length;lin += 1) {
            accumulatedSum += placar[lin][col]
        }
    }
    
    return accumulatedSum > 0
}