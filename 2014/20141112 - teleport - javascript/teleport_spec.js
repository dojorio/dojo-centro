var assert = require('assert'),
    teleport = require('./teleport').teleport

describe('Teleporte', function () {
    context('1 nave viagem de 1 para 1,', function () {
        var origem, destino;

        beforeEach(function(){
            origem = destino = 1
            paineis = [[1, 1, 1, 1]]
        })

        it('duro, 1 caminho', function() {
            var $ = 0,
                result = teleport($, origem, destino, paineis)

            assert.equal(result, 1)
        })

        it('com $1, 4 caminhos', function() {
            var $ = 1,
                result = teleport($, origem, destino, paineis)

            assert.equal(result, 4)
        })

        it('com 2$, 16 caminhos', function() {
            var $ = 2,
                result = teleport($, origem, destino, paineis)

            assert.equal(result, 16)
        })

        it('com 3$', function() {
            var $ = 3,
                result = teleport($, origem, destino, paineis)

            assert.equal(result, 64)
        })
    })

    context('2 naves', function () {
        context('viagem de 1 para 1,', function () {
            var origem, destino;

            beforeEach(function(){
                origem = destino = 1
            })

            it('com 1$', function() {
                var paineis = [[2, 2, 2, 2], [2, 2, 2, 2]],
                    result = teleport(1, origem, destino, paineis)

                assert.equal(result, 0)
            })

            it('com 1$ sendo o primeiro diferente', function() {
                var paineis = [[1, 2, 2, 2], [2, 2, 2, 2]],
                    result = teleport(1, origem, destino, paineis)

                assert.equal(result, 1)
            })

            it('com 1$ sendo o primeiro e segundo diferentes', function() {
                var paineis = [[1, 1, 2, 2], [2, 2, 2, 2]],
                    result = teleport(1, origem, destino, paineis)

                assert.equal(result, 2)
            })

            it('com 1$ sendo o primeiro,segundo e ultimo diferentes', function() {
                var paineis = [[1, 1, 2, 1], [2, 2, 2, 2]],
                    result = teleport(1, origem, destino, paineis)

                assert.equal(result, 3)
            })

            it('com 1$ sendo o todos diferentes', function() {
                var paineis = [[1, 1, 1, 1], [2, 2, 2, 2]],
                    result = teleport(1, origem, destino, paineis)

                assert.equal(result, 4)
            })
         
            it('com 2$ sendo todos iguais', function() {
                var paineis = [[1, 1, 1, 1], [2, 2, 2, 2]],
                    result = teleport(2, origem, destino, paineis)

                assert.equal(result, 16)
            })
        })

        context('viagem de 1 para 2,', function () {
            var origem, destino;

            beforeEach(function(){
                origem = 1
                destino = 2
            })

            it('com 1$ sendo todos iguais', function() {
                var paineis = [[1, 1, 1, 1], [2, 2, 2, 2]],
                    result = teleport(1, origem, destino, paineis)

                assert.equal(result, 0)
            })

            it('com 1$ sendo todos 2', function() {
                var paineis = [[2, 2, 2, 2], [2, 2, 2, 2]],
                    result = teleport(1, origem, destino, paineis)

                assert.equal(result, 4)
            })
        })
    })



})
