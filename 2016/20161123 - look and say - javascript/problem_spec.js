var assert = require ('assert'),
    lookNSay = require('./problem').lookNSay;

describe('when we look 1', function() {
    it('we say 11', function () {
        assert.strictEqual(lookNSay(1), 11)
    })
})

describe('when we look 2', function() {
    it('we say 12', function () {
        assert.strictEqual(lookNSay(2), 12)
    })
})

describe('when we look 21', function() {
    it('we say 1211', function () {
        assert.strictEqual(lookNSay(21), 1211)
    })
})

describe('when we look 22', function() {
    it('we say 22', function () {
        assert.strictEqual(lookNSay(22), 22)
    })
})

