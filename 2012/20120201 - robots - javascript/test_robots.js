module("Robots")


test("deve movimentar para o norte", function(){
        var posicao_final = comanda([1, 2, 'N'], 'M');
        same(posicao_final, [1, 3, 'N'])
    }
);

test("deve movimentar para sul", function(){
        var posicao_final = comanda([1, 2, 'S'], 'M');
        same(posicao_final, [1, 1, 'S'])
    }
);

test("deve movimentar para oeste", function(){
    var posicao_final = comanda([1, 2, 'W'], 'M');
    same(posicao_final, [0, 2, 'W'])
})

test("deve virar para a esquerda do oeste", function(){
        var posicao_final = comanda([1, 2, 'W'], 'L');
        same(posicao_final, [1, 2, 'S'])
    }
);

test("deve virar 90 graus pra esquerda", function(){
        var posicao_final = comanda([1, 2, 'N'], 'L');
        same(posicao_final, [1, 2, 'W'])
    }
);

test("deve virar 90 graus pra direita", function(){
        var posicao_final = comanda([1, 2, 'N'], 'R');
        same(posicao_final, [1, 2, 'E'])
    }
);

test("Quando estiver apontando para o oeste e receber o comando 'R' deve apontar para o norte  ", function(){
        var posicao_final = comanda([1, 2, 'W'], 'R');
        same(posicao_final, [1, 2, 'N'])
    }
);
