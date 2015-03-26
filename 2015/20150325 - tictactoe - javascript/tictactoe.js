exports.tictactoe = function (tabuleiro) {
    if (tabuleiro[0] == 'XXX') {
        return 'X';
    }

    if (tabuleiro[0].indexOf('.') != -1) {
        return 'incompleto';
    }
    if (tabuleiro[1].indexOf('.') != -1) {
        return 'incompleto';
    }
    if (tabuleiro[2].indexOf('.') != -1) {
        return 'incompleto';
    }
    return 'velha';
}