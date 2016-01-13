var assert = require ('assert'),
    imperialism = require('./imperialism');

describe('imperialism.conquer', function() {
    it('1 empires', function () {
        var roads = []
        assert.equal(imperialism.conquer(roads), 0)
    })

    it('2 empires', function () {
        var roads = [1]
        assert.equal(imperialism.conquer(roads), 1)
    })

    it('3 empires, all connecting to 1', function () {
        var roads = [1, 1]
        assert.equal(imperialism.conquer(roads), 1)
    })

    it('3 empires', function () {
        var roads = [1, 2]
        assert.equal(imperialism.conquer(roads), 1)
    })

    it('4 empires', function () {
        var roads = [1, 2, 3]
        assert.equal(imperialism.conquer(roads), 2)
    })

    it('4 empires, all connecting to 1', function () {
        var roads = [1, 1, 1]
        assert.equal(imperialism.conquer(roads), 1)
    })

    it('1 2 2 4 5', function () {
        var roads = [1, 2, 2, 4, 5]
        assert.equal(imperialism.conquer(roads), 2)
    })

    it('1 1 3 3 4 4', function () {
        var roads = [1, 1, 3, 3, 4, 4]
        assert.equal(imperialism.conquer(roads), 2)
    })

    it('1 2 3 1 2 3 5 6 1 3 4 2 1 8 9 7 1 1 3 4 5', function () {
        var roads = [1, 2, 3, 1, 2, 3, 5, 6, 1, 3, 4, 2, 1, 8, 9, 7, 1, 1, 3, 4, 5]
        assert.equal(imperialism.conquer(roads), 4)
    })

    
});

describe('imperialism.toGraph', function () {
    it('1 empire', function () {
        var roads = [];
        var graph = {
            1: []
        };
        assert.deepEqual(imperialism.toGraph(roads), graph)
    })

    it('2 empires', function () {
        var roads = [1];
        var graph = {
            1: [2], 
            2: [1]
        };
        assert.deepEqual(imperialism.toGraph(roads), graph)
    })

    it('3 empires', function () {
        var roads = [1, 1];
        var graph = {
            1: [2, 3], 
            2: [1],
            3: [1]
        };
        assert.deepEqual(imperialism.toGraph(roads), graph)
    })
})

describe('imperialism.collapse', function () {
    it('2 empires collapse 1', function () {
        var graph = {
            1: [2], 
            2: [1]
        };
        assert.deepEqual(imperialism.collapse(graph, 1), { 1: [] }) 
    })

    it('2 empires collapse 2', function () {
        var graph = {
            1: [2], 
            2: [1]
        };
        assert.deepEqual(imperialism.collapse(graph, 2), { 2: [] }) 
    })

    it('3 empires collapse 1', function () {
        var graph = {
            1: [2], 
            2: [1, 3],
            3: [2]
        };
        var expected = {
            1: [3],
            3: [1]
        };
        assert.deepEqual(imperialism.collapse(graph, 1), expected) 
    })

    it('6 empires collapse 2', function () {
        var graph = {
            1: [2], 
            2: [1, 3, 4],
            3: [2],
            4: [2, 5], 
            5: [4, 6],
            6: [5]
        };
        var expected = {
            2: [5],
            5: [2, 6],
            6: [5]
        };
        assert.deepEqual(imperialism.collapse(graph, 2), expected) 
    })
})