var assert = require ('assert'),
	bye = 'tchau, querida!',
	stay = 'não vai ter golpe!',
    dilma_boolean = require('./dilma_boolean').dilma_boolean

describe('Dilma boolean case', function() {
    it('one for yes', function () {
        var intentions = 's'
        assert.equal(dilma_boolean(intentions), bye)
    })

    it('one for no', function () {
        var intentions = 'n'
        assert.equal(dilma_boolean(intentions), stay)
    })

    it('one influent for no', function () {
        var intentions = 'N'
        assert.equal(dilma_boolean(intentions), stay)
    })

    it('two for no', function () {
        var intentions = 'nn'
        assert.equal(dilma_boolean(intentions), stay)
    })

    it('one for each', function () {
        var intentions = 'ns'
        assert.equal(dilma_boolean(intentions), stay)
    })

    it('two for s andonefor n', function () {
        var intentions = 'ssn'
        assert.equal(dilma_boolean(intentions), bye)
    })

    it('two for s andonefor n', function () {
        var intentions = 'sssn'
        assert.equal(dilma_boolean(intentions), bye)
    })

    it('S influences n', function () {
        var intentions = 'sSnn'
        assert.equal(dilma_boolean(intentions), bye)
    })

    it('S influences n and not the last n', function () {
        var intentions = 'sSnnn'
        assert.equal(dilma_boolean(intentions), bye)
    })

    it('N influences s', function () {
        var intentions = 'Nss'
        assert.equal(dilma_boolean(intentions), stay)
    })

    it('S not influences N', function () {
        var intentions = 'SN'
        assert.equal(dilma_boolean(intentions), stay)
    })

    it('SnNs', function () {
        var intentions = 'SnNs'
        assert.equal(dilma_boolean(intentions), stay)
    })
})