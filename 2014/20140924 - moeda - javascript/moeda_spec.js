var assert = require('assert'),
    troco = require('./moeda').troco

describe("Moeda", function() {
    it("uma moeda 1 para o mesmo valor", function() {
        assert.equal(troco([1], 1), 1)
    })

    it("uma moeda 1 para valor maior", function() {
        assert.equal(troco([1], 3), 3)
    })

    it("uma moeda 2 para o mesmo valor", function() {
        assert.equal(troco([2], 2), 1)
    })

    it("uma moeda 2 para valor maior", function() {
        assert.equal(troco([2], 4), 2)
    })

    it("uma moeda 3 para o mesmo valor", function() {
        assert.equal(troco([3], 3), 1)
    })

    it("uma moeda 3 para valor maior", function() {
        assert.equal(troco([3], 9), 3)
    })

    it(" moedas 1,3 para valor 3", function() {
        assert.equal(troco([1, 3], 3), 1)
    })

    it(" moedas 1,2 para valor 3", function() {
        assert.equal(troco([1, 2], 3), 1)
    })
})