var assert = require ('assert'),
    problem = require('./problem').problem;

describe('problem', function() {
    it('sample', function () {
        var bar = []
        assert.equal(problem(bar), 0)
    })
})