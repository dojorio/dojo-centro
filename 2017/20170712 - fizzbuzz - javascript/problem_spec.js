var assert  = require('assert'),
    fizzbuzz = require('./problem').fizzbuzz;

describe('fizzbuzz', function() {
    it('return of 1', function () {
        assert.equal(fizzbuzz(1), 1)
    })
    it('return of 2', function () {
        assert.equal(fizzbuzz(2), 2)
    })
})