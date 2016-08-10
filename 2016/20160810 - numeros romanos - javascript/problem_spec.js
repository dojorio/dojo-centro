var assert = require ('assert'),
    to_roman = require('./problem').to_roman;

describe('Números romanos', function() {
    it('transforma 1', function () {
        assert.equal(to_roman(1), 'I')
    })

    it('transforma 2', function () {
        assert.equal(to_roman(2), 'II')
    })

    it('transforma 3', function () {
        assert.equal(to_roman(3), 'III')
    })

	it('transforma 4', function () {
        assert.equal(to_roman(4), 'IV')
    })

    it('transforma 5', function () {
        assert.equal(to_roman(5), 'V')
    })


})