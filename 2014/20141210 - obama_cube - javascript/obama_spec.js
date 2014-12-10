var assert = require('assert'),
    obama  = require('obama')

describe('Obama', function() {
    context('compara 2 cubos', function() {
        it('111111 e 111111', function() {
            assert.equal(distinct_cubes(['111111', '111111']), 1)
        })
    })
})