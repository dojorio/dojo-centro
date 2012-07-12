module('Guerra');

test('se A é amigo de B, A é amigo de B', function() {
    var relacoes = [amigo1('A', 'B')];
    var pessoas = ['A', 'B'];
    
    var resultado = avaliador1(relacoes, pessoas, 'amigo');
    same(resultado, true);
});

test('se A é amigo de B, eles nao sao inimigos', function() {
    var relacoes = [amigo1('A', 'B')];
    var pessoas = ['A', 'B'];
    
    var resultado = avaliador1(relacoes, pessoas, 'inimigo');
    same(resultado, false);
});

test('se nada, A e B não são nada', function() {
    var relacoes = [];
    var pessoas = ['A', 'B'];
    
    var resultado = avaliador1(relacoes, pessoas, 'amigo');
    same(resultado, false);
    
    var resultado = avaliador1(relacoes, pessoas, 'inimigo');
    same(resultado, false);
});

test('se A é inimigo de B e B é amigo de C, B é amigo de C', function() {
    var relacoes = [inimigo('A', 'B'), amigo('B', 'C')]
    var pergunta = amigo('B', 'C');
    var resultado = avaliador(relacoes, pergunta);
    same(resultado, true);
});


test('se A é amigo de B, B não é amigo de C', function() {
    var relacoes = [amigo('A', 'B')];
    var pergunta = amigo('B', 'C');
    var resultado = avaliador(relacoes, pergunta);
    same(resultado, false);
});

test('se A é amigo de B, B é amigo de A', function() {
    var relacoes = [amigo('A', 'B')];
    var pergunta = amigo('B', 'A');
    var resultado = avaliador(relacoes, pergunta);
    same(resultado, true);
});
