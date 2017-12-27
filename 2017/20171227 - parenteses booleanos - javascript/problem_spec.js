var assert = require ('assert'),
    problem = require('./problem').problem;

// http://www.dojopuzzles.com/problemas/exibe/parenteses-booleanos/

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

        it('true or false', function () {
            var expression = 'true or false'
            assert.equal(problem(expression), 1)
        })

        it('false or true', function () {
            var expression = 'false or true'
            assert.equal(problem(expression), 1)
        })
    })

    context('xor operator', function () {
        it('true xor false', function () {
            var expression = 'true xor false'
            assert.equal(problem(expression), 1)
        })

        it('false xor true', function () {
            var expression = 'false xor true'
            assert.equal(problem(expression), 1)
        })

        it('true xor true', function () {
            var expression = 'true xor true'
            assert.equal(problem(expression), 0)
        })   
    })

    context ('and + and operator', function () {
        it('true and true and true', function () {
            var expression = 'true and true and true'
            assert.equal(problem(expression), 2)
        })
    })

    context ('and + or operator', function () {
        it('true and true or true', function () {
            var expression = 'true and true or true'
            assert.equal(problem(expression), 2)
        })

        it('true or true and true', function () {
            var expression = 'true or true and true'
            assert.equal(problem(expression), 2)
        })
        it('true and true or false', function () {
            var expression = 'true and true or false'
            assert.equal(problem(expression), 2)
        })
        
        it('true and true or false', function () {
            var expression = 'true and true or false'
            assert.equal(problem(expression), 2)
        })
    })





    
})