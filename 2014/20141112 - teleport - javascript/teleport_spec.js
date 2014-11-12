var assert = require('assert'),
    teleport = require('./teleport').teleport

describe('Teleporte', function () {
    it('1 nave viagem de 1 para 1, duro', function() {
        var creditos = 0,
            origem = destino = 1,
            paineis = [[1, 1, 1, 1]],
            result = teleport(creditos, origem, destino, paineis)

        assert.equal(result, 1)
    })
})
