var assert = require ('assert'),
    lookNSay = require('./problem').lookNSay;

describe('when we look 1', () => {
    it('we say 11', () => {
        assert.strictEqual(lookNSay(1), 11)
    })
})

describe('when we look 2', () => {
    it('we say 12', () => {
        assert.strictEqual(lookNSay(2), 12)
    })
})

describe('when we look 21', () => {
    it('we say 1211', () => {
        assert.strictEqual(lookNSay(21), 1211)
    })
})

describe('when we look 22', () => {
    it('we say 22', () => {
        assert.strictEqual(lookNSay(22), 22)
    })
})

describe('when we look 222', () => {
    it('we say 32', () => {
        assert.strictEqual(lookNSay(222), 32)
    })
})
