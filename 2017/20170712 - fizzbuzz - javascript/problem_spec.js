var assert  = require('assert'),
    fizzbuzz = require('./problem').fizzbuzz;

describe('fizzbuzz', function() {
    it('return of 1', function () {
        assert.equal(fizzbuzz(1), 1)
    })
    it('return of 2', function () {
        assert.equal(fizzbuzz(2), 2)
    })
    it('return of 3', function () {
        assert.equal(fizzbuzz(3), 'fizz')
    })
    it('return of 4', function () {
        assert.equal(fizzbuzz(4), 4)
    })

})