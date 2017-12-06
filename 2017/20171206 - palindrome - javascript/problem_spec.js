var assert = require ('assert'),
    problem = require('./problem').problem;

describe('panlidrome', function() {
    it('when "7" returns 0', function () {
        var bar = ["7"]
        assert.equal(problem(bar), 0)
    })

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
    
    it('when "aba" returns 3', function () {
        var bar = ["aba"]
        assert.equal(problem(bar), 3)
    })

    it('when "aaa" returns 3', function () {
        var bar = ["aaa"]
        assert.equal(problem(bar), 3)
    })

    it('when "ananias" returns 0', function () {
        var bar = ["ananias"]
        assert.equal(problem(bar), 0)
    })

    it('when "ananana" returns 7', function () {
        var bar = ["ananana"]
        assert.equal(problem(bar), 7)
    })

})