module('Campominado');

test('Campo 2x2 sem bombas', function() {
    var entrada = [
        [' ', ' '],
        [' ', ' ']
    ];
    
    var resultado = marcaNumeros(entrada);
    var esperado = [
        ['0', '0'],
        ['0', '0']
    ];
    
    same(resultado, esperado);
});

test('Campo 2x2 com uma bomba na primeira posição', function() {
    var entrada = [
        ['*', ' '],
        [' ', ' ']
    ];
    
    var resultado = marcaNumeros(entrada);
    var esperado = [
        ['*', '1'],
        ['1', '1']
    ];
    
    same(resultado, esperado);
});

test('Campo 2x2 com uma bomba na sengunda posição', function() {
    var entrada = [
        [' ', '*'],
        [' ', ' ']
    ];
    
    var resultado = marcaNumeros(entrada);
    var esperado = [
        ['1', '*'],
        ['1', '1']
    ];
    
    same(resultado, esperado);
});

test('Campo 2x2 com duas bombas na primeira linha', function() {
    var entrada = [
        ['*', '*'],
        [' ', ' ']
    ];
    
    var resultado = marcaNumeros(entrada);
    var esperado = [
        ['*', '*'],
        ['2', '2']
    ];
    
    same(resultado, esperado);
});

test('Campo 2x2 com três bombas', function() {
    var entrada = [
        ['*', '*'],
        [' ', '*']
    ];
    
    var resultado = marcaNumeros(entrada);
    var esperado = [
        ['*', '*'],
        ['3', '*']
    ];
    
    same(resultado, esperado);
});

test('Campo 3x3 com uma bomba no canto superior esquerdo', function() {
    var entrada = [
        ['*', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ];
    
    var resultado = marcaNumeros(entrada);
    var esperado = [
        ['*', '1', '0'],
        ['1', '1', '0'],
        ['0', '0', '0']
    ];
    
    same(resultado, esperado);
});

test('Campo 3x3 com uma bomba no canto superior direito', function() {
    var entrada = [
        [' ', ' ', '*'],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ];
    
    var resultado = marcaNumeros(entrada);
    var esperado = [
        ['0', '1', '*'],
        ['0', '1', '1'],
        ['0', '0', '0']
    ];
    
    same(resultado, esperado);
});

test('Campo 3x3 com uma bomba no meio', function() {
    var entrada = [
        [' ', ' ', ' '],
        [' ', '*', ' '],
        [' ', ' ', ' ']
    ];
    
    var resultado = marcaNumeros(entrada);
    var esperado = [
        ['1', '1', '1'],
        ['1', '*', '1'],
        ['1', '1', '1']
    ];
    
    same(resultado, esperado);
});

test('Campo 5x5 com uma bomba no meio', function() {
    var entrada = [
        [' ',' ',' ',' ','*'],
        [' ','*',' ',' ','*'],
        [' ',' ',' ',' ',' '],
        [' ',' ','*',' ',' '],
        [' ',' ',' ',' ',' ']
    ];
    
    var resultado = marcaNumeros(entrada);
    var esperado = [
        ['1','1','1','2','*'],
        ['1','*','1','2','*'],
        ['1','2','2','2','1'],
        ['0','1','*','1','0'],
        ['0','1','1','1','0']
    ];
    
    same(resultado, esperado);
});