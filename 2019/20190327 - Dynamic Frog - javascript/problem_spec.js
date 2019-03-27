var assert      = require('assert'),
    dynamicFrog = require('./problem').dynamicFrog;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/1054

describe('Dynamic frog', function() {
    it('no stones', function () {
        var stones = []
        var riverWidth = 1

        assert.equal(dynamicFrog(riverWidth, stones), 1)
    })

    it('no stones, bigger width', function () {
        var stones = []
        var riverWidth = 2

        assert.equal(dynamicFrog(riverWidth, stones), 2)
    })

    it('no stones, yet bigger width', function () {
        var stones = []
        var riverWidth = 3

        assert.equal(dynamicFrog(riverWidth, stones), 3)
    })

    it('1 stone with distance 1, riverWidth 2', function() {
    	var stones = ['B-1']
    	var riverWidth = 2

    	assert.equal(dynamicFrog(riverWidth, stones), 1)
    })

    it('1 stone with distance 1, riverWidth 3', function() {
    	var stones = ['B-1']
    	var riverWidth = 3

    	assert.equal(dynamicFrog(riverWidth, stones), 2)
    })

    it('1 stone with distance 2, riverWidth 4', function() {
    	var stones = ['B-2']
    	var riverWidth = 4

    	assert.equal(dynamicFrog(riverWidth, stones), 2)
    })

    it('2 stones with distance 2, riverWidth 4', function() {
    	var stones = ['B-2', 'B-2']
    	var riverWidth = 4

    	assert.equal(dynamicFrog(riverWidth, stones), 2)
    })

    it('2 stones with distance 1 and 2, riverWidth 4', function() {
    	var stones = ['B-1', 'B-2']
    	var riverWidth = 4

    	assert.equal(dynamicFrog(riverWidth, stones), 2)
    })

    it('2 stones with distance 1 and 3, riverWidth 4', function() {
    	var stones = ['B-1', 'B-3']
    	var riverWidth = 4

    	assert.equal(dynamicFrog(riverWidth, stones), 2)
    })

	it('3 stones B-1, B-2 and B-3, riverWidth 4', function() {
    	var stones = ['B-1', 'B-2', 'B-3']
    	var riverWidth = 4

    	assert.equal(dynamicFrog(riverWidth, stones), 1)
    })

})