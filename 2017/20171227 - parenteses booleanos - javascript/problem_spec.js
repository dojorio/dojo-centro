var assert = require ('assert'),
    problem = require('./problem').problem;

describe('Parentenses Booleanos', function() {
    it('true', function () {
        var expression = 'true'
        assert.equal(problem(expression), 1)
    })
    it('false', function () {
        var expression = 'false'
        assert.equal(problem(expression), 0)
    })

    context('and operator', function () {
        it('true and true', function () {
            var expression = 'true and true'
            assert.equal(problem(expression), 1)
        })
    })

    context('or operator', function () {
        it('true or true', function () {
            var expression = 'true or true'
            assert.equal(problem(expression), 1)
        })
    })


    
})