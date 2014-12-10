var assert = require('assert'),
    distinct_cubes  = require('./obama').distinct_cubes


describe('Obama', function() {
    context('compara 2 cubos', function() {
        it('111111 e 111111', function() {
            assert.equal(distinct_cubes(['111111', '111111']), 1)
        })

        it('111111 e 011111', function() {
            assert.equal(distinct_cubes(['111111', '011111']), 2)
        })

        it('011111 e 101111', function() {
            assert.equal(distinct_cubes(['011111', '101111']), 1)
        })
    })
})