module('Romanos');


test('Converte símbolos simples', function(){
    same(paraIndoArabico("I"), 1);
    same(paraIndoArabico("V"), 5);
    same(paraIndoArabico("X"), 10);
    same(paraIndoArabico("L"), 50);
    same(paraIndoArabico("C"), 100);
    same(paraIndoArabico("D"), 500);
    same(paraIndoArabico("M"), 1000);
});

test('Converte dois símbolos', function(){
    same(paraIndoArabico("II"), 2);
    same(paraIndoArabico("XX"), 20);
});

test('Converte três símbolos', function(){
    same(paraIndoArabico("CCC"), 300);
    same(paraIndoArabico("MMM"), 3000);
});

test('Converte alguns símbolos diferentes', function(){
    same(paraIndoArabico("VI"), 6);
    same(paraIndoArabico("CX"), 110);
    same(paraIndoArabico("CXV"), 115);
});

test('Converte IV em 4', function(){
    same(paraIndoArabico("IV"), 4);
});

test('Converte IX em 9', function(){
    same(paraIndoArabico("IX"), 9);
});

test('Converte XIV em 14', function(){
    same(paraIndoArabico("XIV"), 14);
});

test('Converte XC em 90', function(){
    same(paraIndoArabico("XC"), 90);
});

test('Converte DIX em 509', function(){
    same(paraIndoArabico("DIX"), 509);
});

