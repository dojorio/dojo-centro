var assert = require ('assert'),
    poker = require('./problem').poker;

describe('poker', function() {
    it('empate sequencias iguais', function () {
        assert.equal(
        	poker(
	        	['2H', '4D', '5S', '6S', '7D'],
	        	['2D', '4H', '5H', '6C', '7C']
	        ),
	    'Empate')
    })
})