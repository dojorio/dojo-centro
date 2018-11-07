var assert = require ('assert'),
    fizzbuzz = require('./problem').fizzbuzz;

describe('fizzbuzz', function() {
    it('quando a entrada for 1 a saida será 1', function () {
        assert.equal(fizzbuzz(1), 1)
    })

    it('quando a entrada for 2 a saida será 2', function () {
        assert.equal(fizzbuzz(2), 2)
    })

    it('quando a entrada for 3 a saida será Fizz', function () {
        assert.equal(fizzbuzz(3), 'Fizz')
    })

    it('quando a entrada for 6 a saida será Fizz', function () {
        assert.equal(fizzbuzz(6), 'Fizz')
    })

    it('quando a entrada for 9 a saida será Fizz', function () {
        assert.equal(fizzbuzz(9), 'Fizz')
    })

    it('quando a entrada for 5 a saida será Buzz', function () {
        assert.equal(fizzbuzz(5), 'Buzz')
    })

    it('quando a entrada for 10 a saida será Buzz', function () {
        assert.equal(fizzbuzz(10), 'Buzz')
    })

    it('quando a entrada for 15 a saida será FizzBuzz', function () {
        assert.equal(fizzbuzz(15), 'FizzBuzz')
    })

    it('quando a entrada for 30 a saida será FizzBuzz', function () {
        assert.equal(fizzbuzz(30), 'FizzBuzz')
    })

    it('quando a entrada for 45 a saida será FizzBuzz', function () {
        assert.equal(fizzbuzz(45), 'FizzBuzz')
    })
})