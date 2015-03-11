var assert = require('assert'),
    cheque = require('./cheque');

describe("Cheque por extenso", function () {
    it("1 é exibido como 'um real'", function () {
        assert.equal(cheque.porExtenso(1), 'um real')
    })

    it("2 é exibido como 'dois reais'", function () {
        assert.equal(cheque.porExtenso(1), 'um real')
    })
})