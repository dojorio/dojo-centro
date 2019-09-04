var assert = require ('assert'),
    problem = require('./problem').encontreOTelefone;

describe('Encontre o telefone', function() {
    // it('sample', function () {
    //     var bar = []
    //     assert.equal(problem(bar), 0)
    // })

	it('A retorna 2', function () {
        assert.equal(problem('A'), 2)
    })

	it('D retorna 3', function () {
        assert.equal(problem('D'), 3)
    })

    it('E retorna 3', function () {
        assert.equal(problem('E'), 3)
    })

    it('F retorna 3', function () {
        assert.equal(problem('F'), 3)
    })	

    it('G retorna 4', function () {
        assert.equal(problem('G'), 4)
    })

    it('H retorna 4', function () {
        assert.equal(problem('H'), 4)
    })

    it('I retorna 4', function () {
        assert.equal(problem('I'), 4)
    })

    it('EI retorna 34', function () {
        assert.equal(problem('EI'), 34)
    })

    it('J retorna 5', function () {
        assert.equal(problem('J'), 5)
    })
})