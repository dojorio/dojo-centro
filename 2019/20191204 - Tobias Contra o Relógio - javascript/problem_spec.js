var assert = require('assert'),
    agenda = require('./problem').agenda;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/2985

describe('Tobias Contra o Relógio', function() {
    it('uma atividade', function () {
        var atividades = [[1, 1]]
        assert.equal(agenda(atividades), 1)
    })

    it('duas atividades', function () {
        var atividades = [[1, 1], [2, 1]]
        assert.equal(agenda(atividades), 2)
    })

    it('duas atividades com conflito', function () {
        var atividades = [[1, 2], [2, 1]]
        assert.equal(agenda(atividades), 1)
    })

    it('duas atividades sem conflito invertida', function () {
        var atividades = [[2, 1], [1, 1]]
        assert.equal(agenda(atividades), 2)
    })

    it('três atividades', function () {
        var atividades = [[1, 1], [2, 1], [3, 1]]
        assert.equal(agenda(atividades), 3)
    })

    it('três atividades com conflito nas duas últimas', function () {
        var atividades = [[1, 1], [2, 2], [3, 1]]
        assert.equal(agenda(atividades), 2)
    })

    it('três atividades com conflito nas duas primeiras', function () {
        var atividades = [[1, 2], [2, 1], [3, 1]]
        assert.equal(agenda(atividades), 2)
    })

    it('quatro atividades', function () {
        var atividades = [[1, 1], [2, 1], [3, 1],[4, 1]]
        assert.equal(agenda(atividades), 4)
    })
})