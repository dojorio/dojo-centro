//https://www.urionlinejudge.com.br/judge/en/problems/view/1428

var assert = require('assert'), 
    nessie = require('./nessie');

describe('Nessie', function() {
    it('3x3', function() {
    	assert.equal(nessie.evenTree([3,3]), 1); 
    })

    it('3x6', function() {
    	assert.equal(nessie.evenTree([3,6]), 2); 
    })


})
