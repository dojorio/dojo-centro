var assert = require ('assert'),
    problem = require('./problem').problem;

describe('Parentenses Booleanos', function() {
    it('True', function () {
        var expression = 'true'
        assert.equal(problem(expression), 1)
    })
    it('false', function () {
        var expression = 'false'
        assert.equal(problem(expression), 0)
    })
})