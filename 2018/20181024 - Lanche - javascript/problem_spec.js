var assert = require ('assert'),
    problem = require('./problem').problem;

describe('Lanche', function() {
    it('quando a entrada é 3 1 o resultado sera 5', function () {
        assert.equal(problem(3, 1), 5)
    })

    it('quando a entrada é 4 1 o resultado sera 2', function () {
        assert.equal(problem(4, 1), 2)
    })

    it('quando a entrada é 3 2 o resultado sera 10', function () {
        assert.equal(problem(3, 2), 10)
    })

    it('quando a entrada é 4 2 o resultado sera 2', function () {
        assert.equal(problem(4, 2), 4)
    })

    it('quando a entrada é 5 1 o resultado sera 1.5', function () {
        assert.equal(problem(5, 1), 1.5)
    })

    it('quando a entrada é 6 1 o resultado sera Entrada Invalida', function () {
        assert.equal(problem(6, 1), 'Entrada Invalida')
    })

	it('quando a entrada é 7 1 o resultado sera Entrada Invalida', function () {
        assert.equal(problem(7, 1), 'Entrada Invalida')
    })

	it("quando a entrada é 3 'a' o resultado sera Entrada Invalida", function () {
        assert.equal(problem(3, 'a'), 'Entrada Invalida')
    })

    it("quando a entrada é 3 'b' o resultado sera Entrada Invalida", function () {
        assert.equal(problem(3, 'b'), 'Entrada Invalida')
    })
})