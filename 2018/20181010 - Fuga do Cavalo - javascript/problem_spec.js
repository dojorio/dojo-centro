var assert     = require('assert'),
    knightRun = require('./problem').knightRun;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/1147

describe('problem', function() {
    it('knight can go 8 cells 1', function () {
        var knight = '3c'
        var pawns = ['7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h']
        assert.equal(knightRun(knight, pawns), 8)
    })

    it('knight can go 7 cells 1', function () {
        var knight = '3c'
        var pawns = ['6a', '7b', '7c', '7d', '7e', '7f', '7g', '7h']
        assert.equal(knightRun(knight, pawns), 7)
    })

    it('knight can go 8 cells 2', function () {
        var knight = '3d'
        var pawns = ['6a', '7b', '7c', '7d', '7e', '7f', '7g', '7h']
        assert.equal(knightRun(knight, pawns), 8)
    })

    it('knight can go 7 cells 2', function () {
        var knight = '3d'
        var pawns = ['7a', '6b', '7c', '7d', '7e', '7f', '7g', '7h']
        assert.equal(knightRun(knight, pawns), 7)
    })

    it('knight can go 7 cells 2', function () {
        var knight = '3e'
        var pawns = ['7a', '7b', '6c', '7d', '7e', '7f', '7g', '7h']
        assert.equal(knightRun(knight, pawns), 7)
    })
})