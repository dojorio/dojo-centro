var assert = require ('assert'),
    tictactoe = require('./tictactoe').tictactoe;

describe('tictactoe', function() {
    it('deu velha', function() {
        var tabuleiro = ['OXO',
                         'XOO',
                         'XOX'];
        assert.equal(tictactoe(tabuleiro), 'velha');
    });

    it('incompleto', function() {
        var tabuleiro = ['...',
                         '.OO',
                         'XOX'];
        assert.equal(tictactoe(tabuleiro), 'incompleto');
    });

    it('incompleto 2', function() {
        var tabuleiro = ['X..',
                         '.OO',
                         'XOX'];
        assert.equal(tictactoe(tabuleiro), 'incompleto');
    });

    it('incompleto 3', function() {
        var tabuleiro = ['.X.',
                         '.OO',
                         'XOX'];
        assert.equal(tictactoe(tabuleiro), 'incompleto');
    });

    it('incompleto 4', function() {
        var tabuleiro = ['.XX',
                         '.OO',
                         'XOX'];
        assert.equal(tictactoe(tabuleiro), 'incompleto');
    });

    it('incompleto na segunda linha', function() {
        var tabuleiro = ['OXX',
                         '.OO',
                         'XOX'];
        assert.equal(tictactoe(tabuleiro), 'incompleto');
    });

    it('incompleto na terceira linha', function() {
        var tabuleiro = ['OXX',
                         'XOO',
                         '.XX'];
        assert.equal(tictactoe(tabuleiro), 'incompleto');
    });

    it('completo X', function() {
        var tabuleiro = ['XXX',
                         'XOO',
                         '.XX'];
        assert.equal(tictactoe(tabuleiro), 'X');
    });

});