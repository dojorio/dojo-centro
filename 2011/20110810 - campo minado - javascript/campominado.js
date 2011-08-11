function contaBombasEmVolta(tabuleiro, linha, coluna) {
    var resultado = 0;
    
    for (var i = (linha - 1); i <= (linha + 1); i++) {
        if (tabuleiro[i] == undefined)
            continue;
                
        for (var j = (coluna - 1); j <= (coluna + 1); j++) {
            if (tabuleiro[i][j] == undefined)
                continue;
                
            if (tabuleiro[i][j] == '*')
                resultado++;
        }
    }
    
    return resultado;
}

function marcaNumeros(tabuleiro) {
    var bombas = 0,
        bomba = '*';
        
    for (var linha in tabuleiro) {
        for (var coluna in tabuleiro[linha]) {
            if (tabuleiro[linha][coluna] != bomba) {
                b = contaBombasEmVolta(tabuleiro, linha, coluna);
                tabuleiro[linha][coluna] = b.toString();
            }
        }
    }
        
    return tabuleiro;
}