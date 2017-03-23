var assert = require('assert'),
    fizzbuzz = require('./problem').fizzbuzz;

describe('fizzbuzz', function() {
    it('is num to num', function () {
        assert.equal(fizzbuzz(1), 1)
        assert.equal(fizzbuzz(2), 2)
        assert.equal(fizzbuzz(4), 4)
    })

    it('is fizz to 3', function () {
        assert.equal(fizzbuzz(3), "fizz")
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

    it('is woof to 14', function ()
    {
    	assert.equal(fizzbuzz(14), "woof");
    })

    it('is fizzbuzz to 15', function ()
    {
    	assert.equal(fizzbuzz(15), "fizzbuzz");
    })

    it('is fizzwoof to 21', function ()
    {
    	assert.equal(fizzbuzz(21), "fizzwoof");
    })

    it('is buzzwoof to 35', function ()
    {
    	assert.equal(fizzbuzz(35), "buzzwoof");
    })

    it('is fizzbuzzwoof to 105', function ()
    {
    	assert.equal(fizzbuzz(105), "fizzbuzzwoof");
    })
})