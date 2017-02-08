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

    it('1x3 com fumaca, ar e aeroporto', function () {
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

    it('1x4 com fumaca, 2 ar e aeroporto', function () {
        var map = ['*..A']
        assert.equal(problem(map), 3)
    })

    it('1x5 com fumaca, 3 ar e aeroporto', function () {
        var map = ['*...A']
        assert.equal(problem(map), 4)
    })

	it('1x4 com fumaca, 2 ar e aeroporto', function () {
        var map = ['.*.A']
        assert.equal(problem(map), 2)
    })

	it('1x5 com fumaca, 3 ar e aeroporto', function () {
        var map = ['.*.A.']
        assert.equal(problem(map), 2)
    })

    it('1x6 com fumaca, 4 ar, aeroporto e ar', function () {
        var map = ['.*..A.']
        assert.equal(problem(map), 3)
    })

    it('1x6 com fumaca, 4 ar, aeroporto e ar', function () {
        var map = ['**..A.']
        assert.equal(problem(map), 3)
    })
    
    it('1x6 com fumaca, 2 ar, 2 aeroporto', function () {
        var map = ['**..AA']
        assert.equal(problem(map), 4)
    })

    it('1x6 com fumaca, 2 ar, 2 aeroporto', function () {
        var map = ['AA..**']
        assert.equal(problem(map), 4)
    })

})