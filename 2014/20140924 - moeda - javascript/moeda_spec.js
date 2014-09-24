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

    it("moedas 1,3 para valor 3", function() {
        assert.equal(troco([1, 3], 3), 1)
    })

    it("moedas 1,2 para valor 3", function() {
        assert.equal(troco([1, 2], 3), 2)
    })

    it("moedas 1,3 para valor 4", function() {
        assert.equal(troco([1, 3], 4), 2)
    })

    it("moedas 1,3 para valor 5", function() {
        assert.equal(troco([1, 3], 5), 3)
    })

    it("moedas 1 para valor 5", function() {
        assert.equal(troco([1], 5), 5)
    })

    it("moedas 1,5 para valor 11", function() {
        assert.equal(troco([1, 5], 11), 3)
    })

    it("moedas 1,5 para valor 10", function() {
        assert.equal(troco([1, 5], 10), 2)
    })
})