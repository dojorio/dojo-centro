var assert = require ('assert'),
    problem = require('./problem').problem;

describe('letradosnumeros', function() {
    it('um retorno 2', function () {
        var numeros = ["um"]
        assert.equal(problem(numeros), 2)
    })
    it('dois retorno 3', function () {
        var numeros = ["dois"]
        assert.equal(problem(numeros), 3)
    })


})