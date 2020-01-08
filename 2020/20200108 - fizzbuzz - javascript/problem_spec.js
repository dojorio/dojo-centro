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

    it('8 is 8', function () {
        assert.equal(fizzBuzz(8), 8)
    })

    it('9 is Fizz', function () {
        assert.equal(fizzBuzz(9), 'Fizz')
    })

    it('10 is Buzz', function () {
        assert.equal(fizzBuzz(10), 'Buzz')
    })

    it('11 is 11', function () {
        assert.equal(fizzBuzz(11), 11)
    })

    it('12 is Fizz', function () {
        assert.equal(fizzBuzz(12), 'Fizz')
    })

    it('15 is FizzBuzz', function () {
        assert.equal(fizzBuzz(15), 'FizzBuzz')
    })

})