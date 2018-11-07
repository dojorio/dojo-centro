var assert = require ('assert'),
    fizzbuzz = require('./problem').fizzbuzz;

describe('fizzbuzz', function() {
    it('quando a entrada for 1 a saida sera 1', function () {
        assert.equal(fizzbuzz(1), 1)
    })

    it('quando a entrada for 2 a saida sera 2', function () {
        assert.equal(fizzbuzz(2), 2)
    })

    it('quando a entrada for 3 a saida sera Fizz', function () {
        assert.equal(fizzbuzz(3), 'Fizz')
    })

    it('quando a entrada for 6 a saida sera Fizz', function () {
        assert.equal(fizzbuzz(6), 'Fizz')
    })
})