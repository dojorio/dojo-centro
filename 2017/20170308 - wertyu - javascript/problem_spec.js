var assert = require ('assert'),
    wertyu = require('./problem').wertyu;

describe('WERTYU', function() {
    context('one letter', function () {
        it('returs left letter', function () {
            assert.equal(wertyu('T'), 'R')
            assert.equal(wertyu('S'), 'A')
            assert.equal(wertyu('N'), 'B')
        })

        it('returns "Q" when message is "W"', function () {
            assert.equal(wertyu('W'), 'Q')
        })

        it('returns "W" when message is "E"', function () {
            assert.equal(wertyu('E'), 'W')
        })

        it('returns "E" when message is "R"', function () {
            assert.equal(wertyu('R'), 'E')
        })
        
    })

    it('returns "QW" when message is "WE"', function () {
        assert.equal(wertyu('WE'), 'QW')
    })

    it('returns "JD" when message is "KF"', function () {
        assert.equal(wertyu('KF'), 'JD')
    })

    it('returns "QW JD" when message is "WE KF"', function () {
        assert.equal(wertyu('WE KF'), 'QW JD')
    })

    it('returns "I AM FINE TODAY." when message is "O S, GOMR YPFSU/"', function () {
        assert.equal(wertyu('O S, GOMR YPFSU;'), 'I AM FINE TODAY.')
    })

    it('returns empty when message is empty, undefined or null', function () {
        assert.equal(wertyu(''), '')
        assert.equal(wertyu(), '')
        assert.equal(wertyu(null), '')
    })
})