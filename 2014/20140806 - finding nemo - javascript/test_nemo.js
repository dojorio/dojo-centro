var assert = require('assert')
	findNemo = require('./nemo');
	
describe('finding nemo',function(){
	it('no walls',function(){
		var walls = [],
			doors = [],
			nemo = [Math.pi, Math.pi];
		assert.equal(findNemo(walls, doors, nemo), 0)
	});
});
