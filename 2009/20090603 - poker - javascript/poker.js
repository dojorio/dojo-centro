var Hand = function(){
    
    this.cards = [];
  
};

var Card = function(kind, value){
    this.kind = kind;
    this.value = value;
};

var Game = function(){
    this.getHand = function(){
        hand = new Hand();
        hand.cards.push(1);
        return hand
        }
        
    this.hasPair = function(hand){
        return true;
    }
};

var Deck = function(){
    this.kinds = ['clubs', 'diamonds', 'spades','hearts'];
    this.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K'];
}