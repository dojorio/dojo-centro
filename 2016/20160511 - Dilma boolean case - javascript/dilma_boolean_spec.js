var assert = require ('assert'),
    dilma_boolean = require('./dilma_boolean').dilma_boolean;

describe('Dilma boolean case', function() {
    it('one for yes', function () {
        var intentions = 's'
        assert.equal(dilma_boolean(intentions), 'tchau, querida!')
    })

    it('one for no', function () {
        var intentions = 'n'
        assert.equal(dilma_boolean(intentions), 'não vai ter golpe!')
    })

    it('one influent for no', function () {
        var intentions = 'N'
        assert.equal(dilma_boolean(intentions), 'não vai ter golpe!')
    })
})