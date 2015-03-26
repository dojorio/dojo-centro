var assert = require ('assert'),
	tictactoe = require('./tictactoe').tictactoe
describe('tictactoe', function() {
	it('deu velha', function() {
		var tabuleiro = ['OXO',
						 'XOO',
						 'XOX'];
        assert.equal(tictactoe(tabuleiro), 'velha');
	});

	it('incompleto', function() {
		var tabuleiro = ['X..',
						 '.OO',
						 'XOX'];
        assert.equal(tictactoe(tabuleiro), 'incompleto');
	});
});