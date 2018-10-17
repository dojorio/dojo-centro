//https://www.urionlinejudge.com.br/judge/pt/problems/view/1109
var assert = require ('assert'),
    testRegex = require('./problem').testRegex;

describe('testRegex', function() {
    it('teste a retornou Y', function () {
    	var input = {
    		exp: '(a)',
    		test: 'a'
    	}
        assert.equal(testRegex(input), 'Y')
    })

    it('teste b retornou N', function () {
    	var input = {
    		exp: '(a)',
    		test: 'b'
    	}
        assert.equal(testRegex(input), 'N')
    })

    it('teste b retornou Y', function () {
    	var input = {
    		exp: '(b)',
    		test: 'b'
    	}
        assert.equal(testRegex(input), 'Y')
    })

    it('teste ab retornou Y', function () {
    	var input = {
    		exp: '(a.b)',
    		test: 'ab'
    	}
        assert.equal(testRegex(input), 'Y')
    })

    it('teste aa retornou Y', function () {
    	var input = {
    		exp: '(a*)',
    		test: 'aa'
    	}
        assert.equal(testRegex(input), 'Y')
    })    
})