exports.contest = function (placar) {

    // var somatorio = 0
    // if(nobodySolvedAllTheProblems(placar)) {
    //     somatorio += 1
    // }
    // if(everyProblemWasSolvedByAtLeastOnePerson(placar)) {
    //     somatorio += 1
    // }
    // if(thereIsNoProblemSolvedByEveryone(placar)) {
    //     somatorio += 1
    // }
    // if(thereIsNoProblemSolvedByEveryone(placar)) {
    //     somatorio += 1
    // }

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
    lista = []
    for(var col = 0; col < placar[0].length; col+= 1) {
        accumulatedSum = 0
        for(var lin = 0; lin < placar.length;lin += 1) {
            accumulatedSum += placar[lin][col]
        }
        lista[col] = accumulatedSum
    }

    return !lista.some(function(element) { return element == 0 })
}

exports.thereIsNoProblemSolvedByEveryone = function (placar) {
    competidores = placar.length

    lista = []
    for(var col = 0; col < placar[0].length; col+= 1) {
        accumulatedSum = 0
        for(var lin = 0; lin < competidores;lin += 1) {
            accumulatedSum += placar[lin][col]
        }
        lista[col] = accumulatedSum
    }

    return !lista.some(function(element) { return element == competidores })

}

exports.everyoneSolvedAtLeastOneProblem = function (placar) {
    var ok = true
    var numberProblems = placar[0].length

    for(var i = 0; ok && i < placar.length; i+= 1) {
        ok = placar[i].some(function(element) {
            return element > 0 
        })
    }

    return ok
}
