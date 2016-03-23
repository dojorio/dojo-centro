//https://www.hackerrank.com/challenges/even-tree
//vertices 2 <= N <= 100

var assert = require ('assert'),
    evenTree = require('./eventree').evenTree;

describe('evenTree', function() {
    it('2 vertices', function () {
    	var edges = [
    		[1, 2]
    	];
        assert.equal(evenTree(edges), 0);
    })
});

