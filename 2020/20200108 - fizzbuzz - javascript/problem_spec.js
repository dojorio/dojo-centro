var assert  = require('assert'),
    fizzBuzz = require('./problem').fizzBuzz;

describe('FizzBuzz', function() {
    it('1 is 1', function () {
        assert.equal(fizzBuzz(1), 1)
    })

    it('2 is 2', function () {
        assert.equal(fizzBuzz(2), 2)
    })

    it('3 is Fizz', function () {
        assert.equal(fizzBuzz(3), 'Fizz')
    })

    it('4 is 4', function () {
        assert.equal(fizzBuzz(4), 4)
    })

    it('5 is Buzz', function () {
        assert.equal(fizzBuzz(5), 'Buzz')
    })

    it('6 is Fizz', function () {
        assert.equal(fizzBuzz(6), 'Fizz')
    })

    it('7 is 7', function () {
        assert.equal(fizzBuzz(7),7)
    })



})