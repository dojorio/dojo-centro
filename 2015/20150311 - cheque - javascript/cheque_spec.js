var assert = require('assert'),
    cheque = require('./cheque');

describe("True in portuguese", function () {
	it("means 'verdadeiro' and I think it's beaultiful", function () {
		meaning = function (boolean) {
			return boolean ? 'verdadeiro' : 'falso'
		}
		assert.equal(meaning(true), 'verdadeiro')
	})
})