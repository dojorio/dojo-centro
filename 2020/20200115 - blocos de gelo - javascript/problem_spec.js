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

    it('1 block 1, require 4', function () {
        var blocks = [1]
        var required = 4
        assert.equal(iceBlock(blocks, required), 4)
    })

    context('2 blocks 1, 2', function () {
        var blocks = [1, 2]

        it('require 2', function () {            
            var required = 2
            assert.equal(iceBlock(blocks, required), 1)
        })

        it('require 3', function () {
            var required = 3
            assert.equal(iceBlock(blocks, required), 2)
        })

        it('require 5', function () {
            var required = 5
            assert.equal(iceBlock(blocks, required), 3)
        })
    })

    context('3 blocks 1, 2, 3', function () {
        var blocks = [1, 2, 3]

        it('require 4', function () {            
            var required = 4
            assert.equal(iceBlock(blocks, required), 2)
        })

        it('require 5', function () {            
            var required = 5
            assert.equal(iceBlock(blocks, required), 2)
        })

        it('require 7', function () {            
            var required = 7
            assert.equal(iceBlock(blocks, required), 3)
        })
    })

     it('problem definition 1', function () {      
            var blocks = [1, 5, 10, 15, 25, 50]      
            var required = 100
            assert.equal(iceBlock(blocks, required), 2)
     })

        it('problem definition 2', function () {      
            var blocks = [1, 5]      
            var required = 103
            assert.equal(iceBlock(blocks, required), 23)
     })

})