exports.contest = function (placar) {
    return placar.length * 2
}

exports.nobodySolvedAllTheProblems = function (placar) {
    return placar[0].some(function(element, index, array) {
        return element == 0
    })
}