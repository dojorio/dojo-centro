var assert = require ('assert'),
    helpNhonho = require('./problem').helpNhonho;

// https://www.urionlinejudge.com.br/judge/en/problems/view/1919

describe('Help Nhonho', function() {
    describe('with 2 digits', function() {
        var digits = 2

        it('with K = 0', function () {
            var k = 0

            assert.deepEqual(helpNhonho(k, digits), [])
        })

        it('with K = 11', function () {
            var k = 11

            assert.deepEqual(helpNhonho(k, digits), [[0, 1]])
        })

        it('with K = 22', function () {
            var k = 22

            assert.deepEqual(helpNhonho(k, digits), [[0, 2]])
        })

        it('with K = 33', function () {
            var k = 33

            assert.deepEqual(helpNhonho(k, digits), [[0, 3], [1, 2]])
        })

        it('with K = 44', function () {
            var k = 44

            assert.deepEqual(helpNhonho(k, digits), [[0, 4], [1, 3]])
        })

        it('with K = 55', function () {
            var k = 55

            assert.deepEqual(helpNhonho(k, digits), [[0, 5], [1, 4], [2, 3]])
        })
    })
})