var assert  = require('assert'),
    bingo = require('./problem').bingo;

//https://www.urionlinejudge.com.br/judge/en/problems/view/1136

describe('Bingo', function() {
    it('N 2, set [0,1]', function () {
        var n = 2,
            set = [0, 1]
        assert.equal(bingo(n, set), false)
    })

    it('N 2, set [0,1,2]', function () {
        var n = 2,
            set = [0, 1, 2]
        assert.equal(bingo(n, set), true)
    })
})