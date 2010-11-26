$(function(){
module("Mictorio");

    test("Banheiro de 3 mictórios sem ninguém", function(){
        banheiro = [0,0,0];
        equals(2, ocupar(banheiro));
    });

    test("Banheiro de 10 mictórios sem ninguém", function(){
        banheiro = [0,0,0,0,0,0,0,0,0,0];
        equals(9, ocupar(banheiro));
    });
    
    test("Banheiro de 3 mictórios com última ocupada", function(){
        banheiro = [0,0,1];
        equals(0, ocupar(banheiro));
    });

    test("Banheiro de 3 mictórios cheio", function(){
        banheiro = [1,0,1];
        equals(-1, ocupar(banheiro));
    });
    
    test("Banheiro de 5 mictórios com uma vaga", function(){
        banheiro = [1,0,0,0,1];
        equals(2, ocupar(banheiro));
    });
    
    test("Banheiro de 5 mictórios com uma vaga", function(){
        banheiro = [1,0,0,0,1];
        equals(2, ocupar(banheiro));
    });
    
});
