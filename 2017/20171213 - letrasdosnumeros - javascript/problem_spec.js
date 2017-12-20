var assert = require ('assert'),
    problem = require('./problem').problem;

describe('letradosnumeros', function() {
    it('um retorno 2', function () {
        var numeros = ["um"]
        assert.equal(problem(numeros), 2)
    })
    it('dois retorno 4', function () {
        var numeros = ["dois"]
        assert.equal(problem(numeros), 4)
    })
    it('um e dois retorno 6 ', function () {
        var numeros = ["um","dois"]
        assert.equal(problem(numeros), 6)
    })
	it('um, dois, três retorno 10', function () {
        var numeros = ["um","dois","três"]
        assert.equal(problem(numeros), 10)
    })
	it('desseis, vinteequatro retorno 19', function () {
        var numeros = ["desseis", "vinteequatro"]
        assert.equal(problem(numeros), 19)
    })


})