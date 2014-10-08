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
    return !placar[0].some(function(element) {
        return element == 0
    })
}