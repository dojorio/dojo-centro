var assert    = require('assert'),
    required  = require('./tictactoe'),
    maryWins  = required.maryWins

describe("tabuleiro 3 casas", function() {
    
    it("'...' Mary ganha", function() {
        assert.equal( maryWins('...') , true)
    })

    it("'.x.' Mary perde", function() {
        assert.equal( maryWins('.x.') , false)
    })

    it("'x..' Mary perde", function() {
        assert.equal( maryWins('x..') , false)
    })

    it("'..x' Mary perde", function() {
        assert.equal( maryWins('..x') , false)
    })

    it("'xx.' Mary ganha", function() {
        assert.equal( maryWins('xx.') , true)
    })

    it("'x.x' Mary ganha", function() {
        assert.equal( maryWins('x.x') , true)
    })

    it("'.xx' Mary ganha", function() {
        assert.equal( maryWins('.xx') , true)
    })
})

describe('tabuleiro com 4 casas', function() {

    it("'....' Mary ganha", function () {
        assert.equal( maryWins('....') , true)
    })

    it("'x...' Mary ganha", function () {
        assert.equal( maryWins('x...') , true)
    })

    it("'...x' Mary ganha", function () {
        assert.equal( maryWins('...x') , true)
    })

    it("'..x.' Mary perde", function () {
        assert.equal( maryWins('..x.') , false)
    })

    it("'x..x' Mary perde", function () {
        assert.equal( maryWins('x..x') , false)
    })
})
