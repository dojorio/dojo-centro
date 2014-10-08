var assert = require('assert'),
    contest = require('./contest').contest,
    nobodySolvedAllTheProblems = require('./contest').nobodySolvedAllTheProblems,
    everyProblemWasSolvedByAtLeastOnePerson = require('./contest').everyProblemWasSolvedByAtLeastOnePerson

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
})