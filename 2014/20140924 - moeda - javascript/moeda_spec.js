var assert = require('assert'),
    troco = require('./moeda').troco

describe("Moeda", function() {
    it("uma moeda para o mesmo valor", function() {
        assert.equal(troco([1], 1), 1)
    })

    it("uma moeda para valor maior", function() {
        assert.equal(troco([1], 3), 3)
    })

    it("uma moeda para o mesmo valor", function() {
        assert.equal(troco([2], 2), 1)
    })
})