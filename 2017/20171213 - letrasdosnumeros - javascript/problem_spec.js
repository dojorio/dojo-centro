var assert = require ('assert'),
    problem = require('./problem').problem;

describe('letradosnumeros', function() {
    it('um retorno 2', function () {
        var bar = ["um"]
        assert.equal(problem(bar), 2)
    })
})