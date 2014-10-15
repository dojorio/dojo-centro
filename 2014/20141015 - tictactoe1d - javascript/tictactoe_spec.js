var assert    = require('assert'),
    required  = require('./tictactoe'),
    maryWins  = required.maryWins

describe("tictactoe 1 d", function() {
    
    it("'...' Mary ganha", function() {
        assert.equal( maryWins('...') , true)
    })

    it("'.x.' Mary perde", function() {
        assert.equal( maryWins('.x.') , false)
    })

    it("'x..' Mary perde", function() {
        assert.equal( maryWins('x..') , false)
    })
})
    
