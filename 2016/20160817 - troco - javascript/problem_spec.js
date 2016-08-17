var assert = require ('assert'),
    troco = require('./problem').troco;

describe('troco', function() {
    it('preco igual pagamento retorna nenhum troco', function () {
        assert.deepEqual(troco(1, 1), {})
    })

    it('preco 1 pagamento 2 retorna uma nota de 1', function () {
        assert.deepEqual(troco(1, 2), { '1' : 1 })
    })

    it('preco 3 pagamento 5 retorna uma nota de 2', function () {
        assert.deepEqual(troco(3, 5), { '2' : 1 })
    })

    it('preco 4 pagamento 5 retorna uma nota de 1', function () {
        assert.deepEqual(troco(4, 5), { '1' : 1 })
    })

    it('preco 1 pagamento 5 retorna duas nota de 2', function () {
        assert.deepEqual(troco(1, 5), { '2' : 2 })
    })

    it('preco 1 pagamento 7 retorna uma nota de 5 e uma de 1', function () {
        assert.deepEqual(troco(1, 7), { '5' : 1, '1' : 1 })
    })

    it('preco 3 pagamento 10 retorna uma nota de 5 e uma de 2', function () {
        assert.deepEqual(troco(3, 10), { '5' : 1, '2' : 1 })
    })

})