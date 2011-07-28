module('Telefone');

test('Telefone sem letras', function() {
    var resultado = getPhoneNumber("1111-1111");
    var esperado = "1111-1111";
    
    same(resultado, esperado);
});

test('Telefone todo de As', function() {
    var resultado = getPhoneNumber("AAAA-AAAA");
    var esperado = "2222-2222";
    
    same(resultado, esperado);
});

test('Telefone todo de Bs', function() {
    var resultado = getPhoneNumber("BBBB-BBBB");
    var esperado = "2222-2222";
    
    same(resultado, esperado);
});

test('Telefone tendo As e Bs', function() {
    var resultado = getPhoneNumber("BABA-ABAB");
    var esperado = "2222-2222";
    
    same(resultado, esperado);
});

test('Telefone tendo As e Bs e Cs', function() {
    var resultado = getPhoneNumber("BABA-CAAB");
    var esperado = "2222-2222";
    
    same(resultado, esperado);
});

test('Telefone tendo D', function() {
    var resultado = getPhoneNumber("DDDD-DDDD");
    var esperado = "3333-3333";
    
    same(resultado, esperado);
});

test('Telefone tendo E', function() {
    var resultado = getPhoneNumber("EEEE-EEEE");
    var esperado = "3333-3333";
    
    same(resultado, esperado);
});


test('Telefone tendo ABCD e Es', function() {
    var resultado = getPhoneNumber("ABCD-EEEE");
    var esperado = "2223-3333";
    
    same(resultado, esperado);
});


test('Telefone tendo ABCDE e Fs', function() {
    var resultado = getPhoneNumber("ABCD-EFFF");
    var esperado = "2223-3333";
    
    same(resultado, esperado);
});


test('Telefone tendo ABCDEF e Gs', function() {
    var resultado = getPhoneNumber("ABCD-EFGG");
    var esperado = "2223-3344";
    
    same(resultado, esperado);
});

test('Telefone tendo 1-HOME-SWEET-HOME', function() {
    var resultado = getPhoneNumber("1-HOME-SWEET-HOME");
    var esperado = "1-4663-79338-4663";
    
    same(resultado, esperado);
});

test('Telefone tendo 0-HOME-SWEET-HOME', function() {
    var resultado = getPhoneNumber("0-HOME-SWEET-HOME");
    var esperado = "0-4663-79338-4663";
    
    same(resultado, esperado);
});


