var assert = require ('assert'),
    problem = require('./problem').problem;

describe('Nuvem de Cinzas', function() {
    it('1x2 com fumaca e aeroporto', function () {
        var map = ['*A']
        assert.equal(problem(map), 1)
    })

    it('1x1 com fumaca', function () {
        var map = ['*']
        assert.equal(problem(map), 0)
    })

    it('1x3 com fumaca, aeroporto e ar', function () {
        var map = ['*.A']
        assert.equal(problem(map), 2)
    })

    it('1x2 com fumaca e ar', function () {
        var map = ['*.']
        assert.equal(problem(map), 0)
    })
    it('1x2 com ar e fumaca', function () {
        var map = ['.*']
        assert.equal(problem(map), 0)
    })

})