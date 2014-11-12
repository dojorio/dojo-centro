var assert = require('assert'),
    teleport = require('./teleport').teleport

describe('Teleporte', function () {
    it('1 nave viagem de 1 para 1, duro, 1 caminho', function() {
        var $ = 0,
            origem = destino = 1,
            paineis = [[1, 1, 1, 1]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 1)
    })

    it('1 nave viagem de 1 para 1, com $1, 4 caminhos', function() {
        var $ = 1,
            origem = destino = 1,
            paineis = [[1, 1, 1, 1]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 4)
    })

    it('1 nave viagem de 1 para 1, com 2$, 16 caminhos', function() {
        var $ = 2,
            origem = destino = 1,
            paineis = [[1, 1, 1, 1]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 16)
    })

    it('1 nave viagem de 1 para 1, com 3$', function() {
        var $ = 3,
            origem = destino = 1,
            paineis = [[1, 1, 1, 1]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 64)
    })

    it('2 nave viagem de 1 para 1, com 1$', function() {
        var $ = 1,
            origem = destino = 1,
            paineis = [[2, 2, 2, 2], [2, 2, 2, 2]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 0)
    })

    it('2 nave viagem de 1 para 1, com 1$ sendo o primeiro diferente', function() {
        var $ = 1,
            origem = destino = 1,
            paineis = [[1, 2, 2, 2], [2, 2, 2, 2]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 1)
    })

    it('2 nave viagem de 1 para 1, com 1$ sendo o primeiro e segundo diferentes', function() {
        var $ = 1,
            origem = destino = 1,
            paineis = [[1, 1, 2, 2], [2, 2, 2, 2]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 2)
    })

    it('2 nave viagem de 1 para 1, com 1$ sendo o primeiro,segundo e ultimo diferentes', function() {
        var $ = 1,
            origem = destino = 1,
            paineis = [[1, 1, 2, 1], [2, 2, 2, 2]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 3)
    })

    it('2 nave viagem de 1 para 1, com 1$ sendo o todos diferentes', function() {
        var $ = 1,
            origem = destino = 1,
            paineis = [[1, 1, 1, 1], [2, 2, 2, 2]],
            result = teleport($, origem, destino, paineis)

        assert.equal(result, 4)
    })
})
