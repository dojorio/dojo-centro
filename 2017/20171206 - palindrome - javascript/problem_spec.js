var assert = require ('assert'),
    problem = require('./problem').problem;

describe('panlidrome', function() {
    it('when "a" returns 1', function () {
        var bar = ["a"]
        assert.equal(problem(bar), 1)
    })

    it('when "ab" returns 0', function () {
        var bar = ["ab"]
        assert.equal(problem(bar), 0)
    })

    it('when "b" returns 1', function () {
        var bar = ["b"]
        assert.equal(problem(bar), 1)
    })
    it('when "7" returns 0', function () {
        var bar = ["7"]
        assert.equal(problem(bar), 0)
    })
})