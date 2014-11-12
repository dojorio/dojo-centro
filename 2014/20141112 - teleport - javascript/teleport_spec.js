var assert = require('assert'),
    teleport = require('./teleport').teleport

describe('Teleporte', function () {
    it('1 nave viagem de 1 para 1, duro', function() {
        var $ = 0,
            origem = destino = 1,
            paineis = [[1, 1, 1, 1]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 1)
    })

    it('1 nave viagem de 1 para 1, com 1$', function() {
        var $ = 1,
            origem = destino = 1,
            paineis = [[1, 1, 1, 1]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 4)
    })

    it('1 nave viagem de 1 para 1, com 2$', function() {
        var $ = 2,
            origem = destino = 1,
            paineis = [[1, 1, 1, 1]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 16)
    })
})
