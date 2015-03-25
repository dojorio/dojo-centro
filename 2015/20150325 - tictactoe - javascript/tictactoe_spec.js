describe(function() {
	it('deu velha', function() {
		var tabuleiro = ['OXO',
						 'XOO',
						 'XOX'];
        assert.equal(tictactoe(tabuleiro), 'velha');
	});
});