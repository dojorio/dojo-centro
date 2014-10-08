var assert = require('assert'),
    contest = require('./contest').contest

describe('Contest', function () {
    it('1 problema 1 competidor 0 feito', function () {
        var placar = [[0]]

        assert.equal(contest(placar), 2)
    })

    it('2 problemas 1 competidor 1 feito', function () {
        var placar = [[0, 1]]

        assert.equal(contest(placar), 2)
    })
})