module('Dependencias');

test('Nada depende de nada', function() {
    var dependencias_diretas = {};
    var resultado_esperado = {};
    same(dependencias(dependencias_diretas), resultado_esperado);
});

test('A depende de nada', function() {
    var dependencias_diretas = { 'A' : [] };
    var resultado_esperado = {'A' : [] };
    same(dependencias(dependencias_diretas), resultado_esperado);
});


test('A depende de B', function() {
    var dependencias_diretas = { 'A' : ['B'] };
    var resultado_esperado = { 'A' : ['B'], 'B': [] };
    same(dependencias(dependencias_diretas), resultado_esperado);
});


test('A depende de B e E', function() {
    var dependencias_diretas = { 
                                'A': ['B'],
                                'B': ['E']
                                };
    var resultado_esperado = {
                               'A': ['B','E'],
                               'B': ['E'],
                               'E': []
                              };
    same(dependencias(dependencias_diretas), resultado_esperado);
});

test('A depende de B, B depende de C e C não possui dependencias', function() {
    var dependencias_diretas = { 
                                'A': ['B'],
                                'B': ['C']
                                };
    var resultado_esperado = {
                               'A': ['B','C'],
                               'B': ['C'],
                               'C': [],
                              };
    same(dependencias(dependencias_diretas), resultado_esperado);
});

test('X depende de Y', function() {
    var dependencias_diretas = { 
                                'X': ['Y']
                                };
    var resultado_esperado = {
                               'X': ['Y'],
                               'Y': []
                              };
    same(dependencias(dependencias_diretas), resultado_esperado);
});


test('A depende de B, B depende de C e C depende de D', function() {
    var dependencias_diretas = { 
                                'A': ['B'],
                                'B': ['C'],
                                'C': ['D']
                                };
    var resultado_esperado = {
                               'A': ['B','C', 'D'],
                               'B': ['C', 'D'],
                               'C': ['D'],
                               'D': []
                              };
    same(dependencias(dependencias_diretas), resultado_esperado);
});

