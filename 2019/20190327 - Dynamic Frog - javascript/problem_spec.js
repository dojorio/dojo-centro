var assert      = require('assert'),
    dynamicFrog = require('./problem').dynamicFrog;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/1054

describe('Dynamic frog', function() {
    it('no stones', function () {
        var stones = []
        var riverWidth = 1

        assert.equal(dynamicFrog(riverWidth, stones), 1)
    })

    it('no stones, bigger width', function () {
        var stones = []
        var riverWidth = 2

        assert.equal(dynamicFrog(riverWidth, stones), 2)
    })

    it('no stones, yet bigger width', function () {
        var stones = []
        var riverWidth = 3

        assert.equal(dynamicFrog(riverWidth, stones), 3)
    })
})