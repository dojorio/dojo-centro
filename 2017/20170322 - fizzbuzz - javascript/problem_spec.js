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

    it('is 4 to 4', function () {
        assert.equal(fizzbuzz(4), 4)
    })

    it('is buzz to 5', function () {
        assert.equal(fizzbuzz(5), "buzz");
    })

    it('is fizz to 6', function ()
    {
    	assert.equal(fizzbuzz(6), "fizz");
    })

    it('is woof to 7', function ()
    {
    	assert.equal(fizzbuzz(7), "woof");
    })

    it('is fizz to 9', function ()
    {
    	assert.equal(fizzbuzz(9), "fizz");
    })

    it('is buzz to 10', function ()
    {
    	assert.equal(fizzbuzz(10), "buzz");
    })

    it('is fizz to 12', function ()
    {
    	assert.equal(fizzbuzz(12), "fizz");
    })

    it('is fizzbuzz to 15', function ()
    {
    	assert.equal(fizzbuzz(15), "fizzbuzz");
    })
})