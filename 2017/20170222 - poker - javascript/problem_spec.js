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

    it('primeiro carta mais alta ultima posicao', function () {
        assert.equal(
        	poker(
	        	['2H', '4D', '5S', '6S', '10S'],
	        	['2D', '4H', '5H', '6C', '7C']
	        ),
	    'Primeiro')
    })

    it('primeiro carta mais alta penultima posicao', function () {
        assert.equal(
        	poker(
	        	['2H', '4D', '5S', '10S', '6S'],
	        	['2D', '4H', '5H', '6C', '7C']
	        ),
	    'Primeiro')
    })

    it('primeiro carta mais alta penultima posicao', function () {
        assert.equal(
        	poker(
	        	['2D', '4H', '5H', '6C', '7C'],
	        	['2H', '4D', '5S', '10S', '6S']
	        ),
	    'Segundo')
    })

    it('o par ganha', function () {
        assert.equal(
        	poker(
	        	['2D', '2H', '5H', '6C', '7C'],
	        	['2H', '4D', '5S', '10S', '6S']
	        ),
	    'Primeiro')
    })
})