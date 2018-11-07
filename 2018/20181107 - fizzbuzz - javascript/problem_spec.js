var assert = require ('assert'),
    problem = require('./problem').problem;

describe('problem', function() {
    it('quando a entrada for 1 a saida sera 1', function () {
        var input = 1;
        assert.equal(problem(input), 1)
    })
})