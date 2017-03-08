var assert = require ('assert'),
    wertyu = require('./problem').wertyu;

describe('WERTYU', function() {
    it('returns "Q" when message is "W"', function () {
        assert.equal(wertyu('W'), 'Q')
    })

    it('returns empty when message is empty', function () {
        assert.equal(wertyu(''), '')
    })

    it('returns empty when message is undefined', function () {
        assert.equal(wertyu(), '')
    })
})