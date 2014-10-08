var assert = require('assert'),
    contest = require('./contest').contest

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

    it('2 problemas 1 competidor 2 feito', function () {
        var placar = [
            [1, 0],
            [0, 0]
        ]

        assert.equal(contest(placar), 2)
    })
})