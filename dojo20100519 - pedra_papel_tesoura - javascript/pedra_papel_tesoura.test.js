$(function(){
module("Pedra, Papel e Tesoura");

test("Somente um jogador joga papel e ganha", function() {
    jogador1 = {"nome":"A","jogada":"papel"};
    same(jokenpo([jogador1]),["A"]);
});

test("Somente um jogador joga tesoura e ganha", function() {
    jogador1 = {"nome":"B","jogada":"tesoura"};
    same(jokenpo([jogador1]),["B"]);
});


test("Dois jogadores, jogam papel e da empate", function() {
    jogador1 = {"nome":"C","jogada":"papel"};
    jogador2 = {"nome":"D","jogada":"papel"};
    same(jokenpo([jogador1, jogador2]),["C","D"]);
});

test("Dois jogadores, jogam tesoura e da empate", function() {
    jogador1 = {"nome":"E","jogada":"tesoura"};
    jogador2 = {"nome":"F","jogada":"tesoura"};
    same(jokenpo([jogador1, jogador2]),["E","F"]);
});

test("Dois jogadores, jogam tesoura e papel e tesoura ganha", function() {
    jogador1 = {"nome":"G","jogada":"tesoura"};
    jogador2 = {"nome":"H","jogada":"papel"};
    same(jokenpo([jogador1, jogador2]),["G"]);
});

test ("Dois jogadores, jogam papel e tesoura e tesoura ganha", function(){
    jogador1 = new Jogador("I", "papel");
    jogador2 = new Jogador("J", "tesoura")
    same(jokenpo([jogador1, jogador2]),["J"]);
});

test ("Dois jogadores, jogam papel e pedra e papel ganha", function(){
    jogador1 = new Jogador("I", "papel");
    jogador2 = new Jogador ("J", "pedra");
    jokenpo = jokenpo([jogador1, jogador2]);
    same(jokenpo,["I"]);
     });

});

