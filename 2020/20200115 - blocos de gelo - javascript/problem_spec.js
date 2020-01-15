var assert = require ('assert'),
    iceBlock = require('./problem').iceBlock;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/1034

describe('iceBlock', function() {
    it('1 block 1, require 1', function () {
        var blocks = [1]
        var required = 1
        assert.equal(iceBlock(blocks, required), 1)
    })

    it('1 block 1, require 2', function () {
        var blocks = [1]
        var required = 2
        assert.equal(iceBlock(blocks, required), 2)
    })

    it('1 block 1, require 3', function () {
        var blocks = [1]
        var required = 3
        assert.equal(iceBlock(blocks, required), 3)
    })
})