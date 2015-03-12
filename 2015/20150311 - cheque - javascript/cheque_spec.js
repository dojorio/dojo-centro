var assert = require('assert'),
    cheque = require('./cheque');

describe("Cheque por extenso", function () {
    it("1 é exibido como 'um real'", function () {
        assert.equal(cheque.porExtenso(1), 'um real')
    })

    it("2 é exibido como 'dois reais'", function () {
        assert.equal(cheque.porExtenso(2), 'dois reais')
    })

    it("3 é exibido como 'três reais'", function () {
        assert.equal(cheque.porExtenso(3), 'três reais')
    })

    it("4 é exibido como 'quatro reais'", function () {
        assert.equal(cheque.porExtenso(4), 'quatro reais')
    })

    it("5 é exibido como 'cinco reais'", function () {
        assert.equal(cheque.porExtenso(5), 'cinco reais')
    })

    it("19 é exibido como 'dezenove reais'", function () {
        assert.equal(cheque.porExtenso(19), 'dezenove reais')
    })

    it("20 é exibido como 'vinte reais'", function () {
        assert.equal(cheque.porExtenso(20), 'vinte reais')
    })

    it("21 é exibido como 'vinte e um reais'", function () {
        assert.equal(cheque.porExtenso(21), 'vinte e um reais')
    })

    it("22 é exibido como 'vinte e dois reais'", function () {
        assert.equal(cheque.porExtenso(22), 'vinte e dois reais')
    })

    it("30 é exibido como 'trinta reais'", function () {
        assert.equal(cheque.porExtenso(30), 'trinta reais')
    })

    it("33 é exibido como 'trinta e três reais'", function () {
        assert.equal(cheque.porExtenso(33), 'trinta e três reais')
    })

    it("40 é exibido como 'quarenta reais'", function () {
        assert.equal(cheque.porExtenso(40), 'quarenta reais')
    })
})