var assert   = require('assert'),
    box_book = require('./problem').box_book;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/1122

describe('Livro Caixa', function() {
    it('is "+" to total 1 and list [1]', function () {
        var list  = [1]
        var total = 1
        assert.equal(box_book(total, list), '+')
    })

    it('is "-" to total -1 and list [1]', function () {
        var list  = [1]
        var total = -1
        assert.equal(box_book(total, list), '-')
    })

    it('is "*" to total 2 and list [1]', function () {
        var list  = [1]
        var total = 2
        assert.equal(box_book(total, list), '*')
    })

    it('is "++" to total 2 and list [1,1]', function () {
        var list  = [1,1]
        var total = 2
        assert.equal(box_book(total, list), '++')
    })
  
    it('is "*" to total 1 and list [2]', function () {
        var list  = [2]
        var total = 1
        assert.equal(box_book(total, list), '*')
    })

    it('is "*" to total -2 and list [1]', function () {
        var list  = [1]
        var total = -2
        assert.equal(box_book(total, list), '*')
    })
    it('is "-+" to total 1 and list [1,2]', function () {
        var list  = [1,2]
        var total = 1
        assert.equal(box_book(total, list), '-+')
    })
})