var assert = require('assert'),
    miojo = require('./miojo').miojo

describe('Miojo', function() {
    it('3min', function () {
        assert.equal(miojo(3), 3)
    })
})