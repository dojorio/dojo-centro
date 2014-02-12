var assert = require('assert');
var roleta = require('../roleta');

describe('Roleta', function(){
    context('3 casas 1 bolinha', function(){
        it('tudo 0', function(){
            casas = [0,0,0]
            bolinhas = [0]
            assert.equal(roleta(casas, bolinhas), 0);
        });

        it('uma casa 1 bolinha -1', function(){
            casas = [1,0,0]
            bolinhas = [-1]
            assert.equal(roleta(casas, bolinhas), 1);
        });
    })
    
});
