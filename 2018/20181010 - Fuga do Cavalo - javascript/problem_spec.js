var assert     = require('assert'),
    knightRun = require('./problem').knightRun;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/1147

describe('problem', function() {
    it('free knight 1', function () {
        var knight = '3c'
        var pawns = ['7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h']
        assert.equal(knightRun(knight, pawns), 8)
    })
})