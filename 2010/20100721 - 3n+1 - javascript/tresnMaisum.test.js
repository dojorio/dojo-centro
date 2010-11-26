$(function(){
module("3n + 1");
test("201 2", function() {
    equals( testeSequencia(201,2),"201 2 0" ,"teste" );
});

test("1 1", function() {
    equals( testeSequencia(1,1),"1 1 1" ,"teste" );
});

test("1 2", function() {
    equals( testeSequencia(1,2),"1 2 2" ,"teste" );
});

test("1 3", function() {
    equals( testeSequencia(1,3),"1 3 8" ,"teste" );
});

test("1 4", function() {
    equals( testeSequencia(1,4),"1 4 8" ,"teste" );
});

test("1 10", function() {
    equals( testeSequencia(1,10),"1 10 20" ,"teste" );
});

test("100 200", function() {
    equals( testeSequencia(100,200),"100 200 125" ,"teste" );
});

test("201 210", function() {
    equals( testeSequencia(201,210),"201 210 89" ,"teste" );
});

test("1073741824 1073741824", function() {
    equals( testeSequencia(1073741824,1073741824),"1073741824 1073741824 31" ,"teste" );
});
});

