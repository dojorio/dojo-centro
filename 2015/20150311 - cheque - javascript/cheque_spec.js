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
})