var assert   = require('assert'),
    fizzbuzz = require('./problem').fizzbuzz;

describe('fizzbuzz', function() {
    it('is 1 for 1', function () {
        assert.equal(fizzbuzz(1), 1)
    })

    it('is 2 for 2', function () {
        assert.equal(fizzbuzz(2), 2)
    })

    it('is "Fizz" for 3', function () {
        assert.equal(fizzbuzz(3), 'Fizz')
    })

    it('is 4 for 4', function () {
        assert.equal(fizzbuzz(4), 4)
    })

    it('is "Buzz" for 5', function () {
        assert.equal(fizzbuzz(5), 'Buzz')
    })

    it('is "Fizz" for 6', function () {
        assert.equal(fizzbuzz(6), 'Fizz')
    })

    it('is 7 for 7', function () {
        assert.equal(fizzbuzz(7), 7)
    })

    it('is 8 for 8', function () {
        assert.equal(fizzbuzz(8), 8)
    })
})