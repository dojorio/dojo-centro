$(function(){
module("Mapa");

test("passo na diagonal começando na primeira posição", function() {
    matriz = [[2, 4],
             [4, 1]];

    mapa = new Mapa(matriz);
    coordenada_atual = [0,0];
    mapa.passo(coordenada_atual);

    same(mapa.proxima_coordenada, [1,1]);
});

test("passo na lateral começando na primeira posição", function() {
    matriz = [[2, 1],
             [4, 4]];

    mapa = new Mapa(matriz);
    coordenada_atual = [0,0];
    mapa.passo(coordenada_atual);

    same(mapa.proxima_coordenada, [0,1]);
});

test("passo pra baixo começando na primeira posição", function() {
    matriz = [[2, 4],
             [1, 4]];

    mapa = new Mapa(matriz);
    coordenada_atual = [0,0];
    mapa.passo(coordenada_atual);

    same(mapa.proxima_coordenada, [1,0]);
});

test("passo pra baixo com valor diferente de 1", function() {
    matriz = [[2, 5],
             [3, 4]];

    mapa = new Mapa(matriz);
    coordenada_atual = [0,0];
    mapa.passo(coordenada_atual);

    same(mapa.proxima_coordenada, [1,0]);
});

test("passo pra direita com valor diferente de um", function() {
    matriz = [[3, 2],
             [6, 4]];

    mapa = new Mapa(matriz);
    coordenada_atual = [0,0];
    mapa.passo(coordenada_atual);

    same(mapa.proxima_coordenada, [0,1]);
});

});

