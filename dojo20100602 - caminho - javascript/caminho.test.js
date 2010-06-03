$(function(){
module("Caminho");

test("passo na diagonal começando na primeira posição", function() {
    matriz = [[2, 4],
             [4, 1]];

    mapa = new Mapa(matriz);
    mapa.passo([0,0]);

    same(mapa.resultado, [1,1]);
});

});

