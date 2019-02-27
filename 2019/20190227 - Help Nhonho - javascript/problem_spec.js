var assert = require ('assert'),
    helpNhonho = require('./problem').helpNhonho;

// https://www.urionlinejudge.com.br/judge/en/problems/view/1919

describe('Help Nhonho', function() {
    describe('with 2 digits', function() {
        var digits = 2

        it('with K = 0', function () {
            var k = 0

            assert.equal(helpNhonho(k, digits).length, 0)
        })

        it('with K = 11', function () {
            var k = 11
            var result = helpNhonho(k, digits)

            assert.equal(result.length, 1)
            assert.equal(result, [[0, 1]])
        })
    })
})