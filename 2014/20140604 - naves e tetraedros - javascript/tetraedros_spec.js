var assert = require('assert');
var tetraedros = require('./tetraedros');

describe('Tetraedros', function () {
    describe('distancias ponto a ponto', function () {
        var pontoAPonto = tetraedros.pontoAPonto
        it('no mesmo eixo', function () {
            var ponto1 = [0, 0, 0],
            ponto2 = [1, 0, 0]

            assert.equal(pontoAPonto(ponto1, ponto2), 1)
        })
        it('no mesmo eixo, só que mais longe', function () {
            var ponto1 = [0, 0, 0],
            ponto2 = [10, 0, 0]

            assert.equal(pontoAPonto(ponto1, ponto2), 10)
        })
    })
})
