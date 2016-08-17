var assert = require ('assert'),
    troco = require('./problem').troco;

describe('troco', function() {
    it('pagamento igual preco retorna nenhum troco', function () {
        assert.deepEqual(troco(1, 1), {})
    })

    it('pagamento 2 preco 1 retorna uma nota de 1', function () {
        assert.deepEqual(troco(1, 2), { '1' : 1 })
    })
})