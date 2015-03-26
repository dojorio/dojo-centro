exports.tictactoe = function (tabuleiro) {
    if (tabuleiro[0].indexOf('.') != -1) {
        return 'incompleto';
    }

    return 'velha';
}