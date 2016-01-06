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

    it('3 empires, all connecting to 1', function () {
        var roads = [1, 1]
        assert.equal(imperialism.conquer(roads), 1)
    })

    it('3 empires', function () {
        var roads = [1, 2]
        assert.equal(imperialism.conquer(roads), 1)
    })

    it('4 empires', function () {
        var roads = [1, 2, 3]
        assert.equal(imperialism.conquer(roads), 2)
    })

    it('4 empires, all connecting to 1', function () {
        var roads = [1, 1, 1]
        assert.equal(imperialism.conquer(roads), 1)
    })
});