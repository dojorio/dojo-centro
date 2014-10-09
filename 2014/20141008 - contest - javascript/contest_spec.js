var assert = require('assert'),
    required = require('./contest'),
    contest = required.contest,
    nobodySolvedAllTheProblems = required.nobodySolvedAllTheProblems,
    everyProblemWasSolvedByAtLeastOnePerson = required.everyProblemWasSolvedByAtLeastOnePerson,
    thereIsNoProblemSolvedByEveryone = required.thereIsNoProblemSolvedByEveryone,
    everyoneSolvedAtLeastOneProblem = required.everyoneSolvedAtLeastOneProblem

/*
    Nobody solved all the problems.
    Every problem was solved by at least one person (not necessarily the same).
    There is no problem solved by everyone.
    Everyone solved at least one problem (not necessarily the same).
*/
describe('Contest', function () {
    it('1 problema 1 competidor 0 feito', function () {
        var placar = [[0]]

        assert.equal(contest(placar), 2)
    })

    it('2 problemas 1 competidor 2 feito', function () {
        var placar = [
            [1, 0],
            [0, 1]
        ]

        assert.equal(contest(placar), 4)
    })

    // it('2 problemas 1 competidor 2 feito', function () {
    //     var placar = [
    //         [1, 0],
    //         [0, 0]
    //     ]

    //     assert.equal(contest(placar), 2)
    // })
})

describe('nobodySolvedAllTheProblems', function () {
    it('1 problema 1 competidor 0 feito', function () {
        var placar = [[0]]
        assert.equal(nobodySolvedAllTheProblems(placar), true)
    })

    it('1 problema 1 competidor 1 feito', function () {
        var placar = [[1]]
        assert.equal(nobodySolvedAllTheProblems(placar), false)
    })

    it('2 problemas 1 competidor 0 feito', function () {
        var placar = [[0, 0]]
        assert.equal(nobodySolvedAllTheProblems(placar), true)
    })

    it('2 problemas 1 competidor 1 feito', function () {
        var placar = [[1, 0]]
        assert.equal(nobodySolvedAllTheProblems(placar), true)
    })

    it('2 problemas 2 competidor 3 feito', function () {
        var placar = [[1, 0],[1,1]]
        assert.equal(nobodySolvedAllTheProblems(placar), false)
    })
})

describe('everyProblemWasSolvedByAtLeastOnePerson', function () {
    it('1 problema 1 competidor 0 feito', function () {
        var placar = [[0]]
        assert.equal(everyProblemWasSolvedByAtLeastOnePerson(placar), false)
    })

    it('1 problema 1 competidor 1 feito', function () {
        var placar = [[1]]
        assert.equal(everyProblemWasSolvedByAtLeastOnePerson(placar), true)
    })

    it('2 problemas 1 competidor 1 feito', function () {
        var placar = [[1, 0]]
        assert.equal(everyProblemWasSolvedByAtLeastOnePerson(placar), false)
    })

    it('1 problema 2 competidores 1 feito', function () {
        var placar = [
            [0],
            [1]
        ]
        assert.equal(everyProblemWasSolvedByAtLeastOnePerson(placar), true)
    })

    it('2 problemas 2 competidores 1 feito', function () {
        var placar = [
            [0, 0],
            [0, 1]
        ]
        assert.equal(everyProblemWasSolvedByAtLeastOnePerson(placar), false)
    })

    it('2 problemas 2 competidores 2 feito', function () {
        var placar = [
            [1, 0],
            [0, 1]
        ]
        assert.equal(everyProblemWasSolvedByAtLeastOnePerson(placar), true)
    })

})

describe("thereIsNoProblemSolvedByEveryone", function(){
    it('1 problema 1 competidor 0 feito', function(){
        var placar = [[0]]
        assert.equal(thereIsNoProblemSolvedByEveryone(placar), true)
    })

    it('1 problema 1 competidor 1 feito', function(){
        var placar = [[1]]
        assert.equal(thereIsNoProblemSolvedByEveryone(placar), false)
    })

    it('1 problema 2 competidores 1 feito', function(){
        var placar = [
            [1],
            [0]
        ]
        assert.equal(thereIsNoProblemSolvedByEveryone(placar), true)
    })

    it('2 problemas 2 competidores 2 feito', function(){
        var placar = [
            [0, 1],
            [1, 0]
        ]
        assert.equal(thereIsNoProblemSolvedByEveryone(placar), true)
    })
})
describe('everyoneSolvedAtLeastOneProblem', function() {
    it('1 problema 1 competidor 0 feito', function() {
        var placar = [[0]]
        assert.equal(everyoneSolvedAtLeastOneProblem(placar), false)
    })

        it('2 problema 2 competidor 2 feito', function() {
        var placar = [
            [0, 1],
            [1, 0]
        ]
        assert.equal(everyoneSolvedAtLeastOneProblem(placar), true)
    })

})
