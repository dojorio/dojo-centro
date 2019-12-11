var assert  = require('assert'),
    tamanhoSubstring = require('./problem').tamanhoSubstring;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/1237

describe('comparação de strings', function() {
    it('a com a', function () {
        var string1 = 'a'
        var string2 = 'a'
        assert.equal(tamanhoSubstring(string1, string2), 1)
    })

    it('a com b', function () {
        var string1 = 'a'
        var string2 = 'b'
        assert.equal(tamanhoSubstring(string1, string2), 0)
    })
})