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
})