$(function(){
module("Jogo de Poker");

test("mao precisa de espaco para cartas", function(){
     hand = new Hand();
     ok(hand.cards, "Tenho mao para cartas");
});

test("Game cria mao", function(){
    game = new Game();
    hand1 = game.getHand();
    ok(hand1.cards.length > 0, "possui cartas");
});

test("Cria carta", function(){
     var card = new Card('clubs', 'A');
     equals(card.kind, 'clubs', "Tenho naipe");
     equals(card.value, 'A',"Tenho valor");
});

test("Encontra Dupla", function(){
    var game = new Game()
    var hand = [new Card('clubs', 'A'), new Card('diamonds', 'A'), new Card('spades', '4'), new Card('spades', '2'), new Card('spades', '3')]
    
    ok(game.hasPair(hand), "Temos uma dupla!");
});

});