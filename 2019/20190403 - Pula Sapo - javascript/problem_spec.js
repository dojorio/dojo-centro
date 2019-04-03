var assert  = require('assert'),
    pulaSapo = require('./problem').pulaSapo;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/1961

describe('Pula Sapo', function () {
    it('pulo 1 alturas 1, 1', function () {
        var alturaPulo = 1
        var alturasCanos = [1, 1]
        assert.equal(pulaSapo(alturaPulo, alturasCanos), 'YOU WIN')
    })

    it('pulo 1 alturas 1, 3', function () {
        var alturaPulo = 1
        var alturasCanos = [1, 3]
        assert.equal(pulaSapo(alturaPulo, alturasCanos), 'GAME OVER')
    })
     it('pulo 1 alturas 2, 3', function () {
        var alturaPulo = 1
        var alturasCanos = [2, 3]
        assert.equal(pulaSapo(alturaPulo, alturasCanos), 'YOU WIN')
    })
    
    it('pulo 1 alturas 2, 4', function () {
        var alturaPulo = 1
        var alturasCanos = [2, 4]
        assert.equal(pulaSapo(alturaPulo, alturasCanos), 'GAME OVER')
    })

    it('pulo 1 alturas 3, 4', function () {
        var alturaPulo = 1
        var alturasCanos = [3, 4]
        assert.equal(pulaSapo(alturaPulo, alturasCanos), 'YOU WIN')
    })

    it('pulo 1 alturas 1, 4', function () {
        var alturaPulo = 1
        var alturasCanos = [1, 4]
        assert.equal(pulaSapo(alturaPulo, alturasCanos), 'GAME OVER')
    })
})