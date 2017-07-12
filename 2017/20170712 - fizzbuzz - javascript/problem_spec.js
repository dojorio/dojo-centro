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
    it('return of 5', function () {
        assert.equal(fizzbuzz(5), 'buzz')
    })
    it('return of 6', function () {
        assert.equal(fizzbuzz(6), 'fizz')
    })
    it('return of 14', function () {
        assert.equal(fizzbuzz(14), 14)
    })
    it('return of 15', function () {
        assert.equal(fizzbuzz(15), 'fizzbuzz')
    })
})