var assert = require ('assert'),
    imperialism = require('./imperialism');

describe('imperialism', function() {
    it('1 empires', function () {
        var roads = []
        assert.equal(imperialism.conquer(roads), 0)
    })

    it('2 empires', function () {
        var roads = [1]
        assert.equal(imperialism.conquer(roads), 1)
    })
});