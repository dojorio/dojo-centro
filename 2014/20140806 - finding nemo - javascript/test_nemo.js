var assert = require('assert')
	findNemo = require('./nemo').findNemo;
	
describe('finding nemo',function(){
	it('no walls',function(){
		var walls = [],
			doors = [],
			nemo = [1.5, 1.5];
		assert.equal(findNemo(walls, doors, nemo), 0)
	});
});
