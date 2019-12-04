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

    it('três atividades', function () {
        var atividades = [[1, 1], [2, 1], [3, 1]]
        assert.equal(agenda(atividades), 3)
    })
})