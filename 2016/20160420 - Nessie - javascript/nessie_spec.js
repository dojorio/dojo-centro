//https://www.urionlinejudge.com.br/judge/en/problems/view/1428

var assert = require('assert'), 
    nessie = require('./nessie');

describe('Nessie', function() {
    it('3x3', function() {
    	assert.equal(nessie.sonar([3,3]), 1); 
    })

    it('3x6', function() {
    	assert.equal(nessie.sonar([3,6]), 2); 
    })

    it('3x4', function() {
    	assert.equal(nessie.sonar([3,4]), 1); 
    })

    it('6x3', function() {
    	assert.equal(nessie.sonar([6,3]), 2); 
    })

    it('7x3', function() {
    	assert.equal(nessie.sonar([7,3]), 2); 
    })

    it('3x7', function() {
    	assert.equal(nessie.sonar([3,7]), 2); 
    })

    it('8x3', function() {
    	assert.equal(nessie.sonar([8,3]), 2); 
    })

    it('3x8', function() {
    	assert.equal(nessie.sonar([3,8]), 2); 
    })

    it('3x9', function() {
    	assert.equal(nessie.sonar([3,9]), 3); 
    })

    it('3x10', function() {
    	assert.equal(nessie.sonar([3,10]), 3); 
    })

    it('3x11', function() {
    	assert.equal(nessie.sonar([3,11]), 3); 
    })

    it('3x12', function() {
    	assert.equal(nessie.sonar([3,12]), 4); 
    })

    it('3x13', function() {
    	assert.equal(nessie.sonar([3,13]), 4); 
    })

    it('9x6', function() {
    	assert.equal(nessie.sonar([9,6]), 6); 
    })

    it('9x7', function() {
    	assert.equal(nessie.sonar([9,7]), 6); 
    })
    it('9x8', function() {
    	assert.equal(nessie.sonar([9,8]), 6); 
    })
    it('9x8', function() {
    	assert.equal(nessie.sonar([9,8]), 7); 
    })
})

