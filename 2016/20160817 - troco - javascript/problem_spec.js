var assert = require ('assert'),
    troco = require('./problem').troco;

describe('troco', function() {
    it('pagamento igual preco retorna nenhum troco', function () {
        assert.deepEqual(troco(1, 1), {})
    })

    it('pagamento 2 preco 1 retorna uma nota de 1', function () {
        assert.deepEqual(troco(1, 2), { '1' : 1 })
    })

    it('pagamento 5 preco 3 retorna uma nota de 2', function () {
        assert.deepEqual(troco(3, 5), { '2' : 1 })
    })

    it('pagamento 5 preco 4 retorna uma nota de 1', function () {
        assert.deepEqual(troco(4, 5), { '1' : 1 })
    })

})