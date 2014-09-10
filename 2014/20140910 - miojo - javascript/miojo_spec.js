var assert = require('assert'),
    miojo = require('./miojo').miojo

describe('Miojo', function() {
    it('3min', function () {
        assert.equal(miojo(3), 3)
    })

    it('4min, 1min', function () {
        assert.equal(miojo(4, 1), 4)
    })

    it('1min, 4min', function(){
        assert.equal(miojo(1, 4), 4)
    })

    it('5min, 3min', function(){
        assert.equal(miojo(5, 3), 3)
    })

    it('5min, 4min', function(){
        assert.equal(miojo(5, 4), 8)
    })

    it('5min, 1min', function(){
        assert.equal(miojo(5, 1), 5)
    })
})