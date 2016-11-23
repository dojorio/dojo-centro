var assert = require ('assert'),
    lookNSay = require('./problem').lookNSay;

describe('when we look 1', function() {
    it('we say 11', function () {
        assert.equal(lookNSay(1), 11)
    })
})

describe('when we look 2', function() {
    it('we say 12', function () {
        assert.equal(lookNSay(2), 12)
    })
})

describe('when we look 21', function() {
    it('we say 1211', function () {
        assert.equal(lookNSay(21), 1211)
    })
})