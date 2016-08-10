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

    it('transforma 10', function () {
        assert.equal(to_roman(10), 'X')
    })

    it('transforma 20', function () {
        assert.equal(to_roman(20), 'XX')
    })

    it('transforma 30', function () {
        assert.equal(to_roman(30), 'XXX')
    })

    it('transforma 9', function () {
        assert.equal(to_roman(9), 'IX')
    })

	it('transforma 11', function () {
        assert.equal(to_roman(11), 'XI')
    })

    it('transforma 6', function () {
        assert.equal(to_roman(6), 'VI')
    })

    it('transforma 7', function () {
        assert.equal(to_roman(7), 'VII')
    })

    it('transforma 8', function () {
        assert.equal(to_roman(7), 'VII')
    })

})