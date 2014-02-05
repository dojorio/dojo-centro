var assert = require('assert');
var cellphone = require('../cellphone');

console.dir(cellphone);
describe('Cellphone', function(){
    context('with one word', function(){
        it('should return 1', function(){
            words = ['banana'];
		    assert.equal(cellphone(words), 1);
	    });
   	});

    context('with two words', function() {
        it('and starting with the same char should return 2', function() {
            words = ['banana', 'brocolis'];
            assert.equal(cellphone(words), 2);
        });
        it('and starting with a different char should return 1', function(){
            words = ['banana', 'maca'];
            assert.equal(cellphone(words), 1);
        }); 
        it('when the first is prefix of the second should be 1.5', function(){
            words = ['banana', 'bananada'];
            assert.equal(cellphone(words), 1.5);
        });
        it('when the second one is prefix of the first one should be 1.5', function(){
            words = ['bananada', 'banana'];
            assert.equal(cellphone(words), 1.5);
        });
    });

    context('with three words', function(){
        it('different from each other', function(){
           words = ['banana','martelo','aviao'];
           assert.equal(cellphone(words),1);
        });

    });
});
