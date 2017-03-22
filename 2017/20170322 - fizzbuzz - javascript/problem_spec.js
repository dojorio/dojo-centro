var assert = require('assert'),
    fizzbuzz = require('./problem').fizzbuzz;

describe('fizzbuzz', function() {
    it('is 1 to 1', function () {
        assert.equal(fizzbuzz(1), 1)
    })

    it('is 2 to 2', function () {
        assert.equal(fizzbuzz(2), 2)
    })

    it('is fizz to 3', function () {
        assert.equal(fizzbuzz(3), "fizz")
    })

    it('is buzz to 5', function () {
        assert.equal(fizzbuzz(5), "buzz")
    })
})