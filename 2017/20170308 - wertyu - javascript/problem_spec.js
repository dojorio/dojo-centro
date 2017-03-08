var assert = require ('assert'),
    wertyu = require('./problem').wertyu;

describe('WERTYU', function() {
    it('returns "Q" when message is "W"', function () {
        assert.equal(wertyu('W'), 'Q')
    })

    it('returns "W" when message is "E"', function () {
        assert.equal(wertyu('E'), 'W')
    })

    it('returns "E" when message is "R"', function () {
        assert.equal(wertyu('R'), 'E')
    })

    it('returns empty when message is empty, undefined or null', function () {
        assert.equal(wertyu(''), '')
        assert.equal(wertyu(), '')
        assert.equal(wertyu(null), '')
    })

})