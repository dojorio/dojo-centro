var assert = require ('assert'),
    problem = require('./problem').problem;

describe('problem', function() {
    it('vazio', function () {
    	var str = ''
        assert.equal(problem(str), '')
    })
    it('A = 2', function () {
    	var str = 'A'
        assert.equal(problem(str), '2')
    })

    it('B = 22', function () {
    	var str = 'B'
        assert.equal(problem(str), '22')
    })
})