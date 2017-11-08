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

    it('N 3, set [0,1,2,3]', function () {
        var n = 3,
            set = [0, 1, 2, 3]
        assert.equal(bingo(n, set), true)
    })

    it('N 4, set [0,1,2,3]', function () {
        var n = 4,
            set = [0, 1, 2, 3 ]
        assert.equal(bingo(n, set), false)
    })

    it('N 4, set [0,1,2,4]', function () {
        var n = 4,
            set = [0, 1, 2, 4 ]
        assert.equal(bingo(n, set), true)
    })
})