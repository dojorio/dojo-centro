$(document).ready(function(){
    describe('Survivor', {
        '1 pessoa e posicao 1 a ser morto': function() {
            var num_pessoas = 1;
            var ordem_morrer = 1;
            var ordem_de_mortos = [];
            value_of(matar(num_pessoas, ordem_morrer)).should_be(ordem_de_mortos);
        },    
        '1 pessoa e posicao qualquer sem mortos': function() {
            var num_pessoas = 1;
            var ordem_morrer = 10;
            var ordem_de_mortos = [];
            value_of(matar(num_pessoas, ordem_morrer)).should_be(ordem_de_mortos);
        },    
        // '6 pessoas e posicao 5 a ser morto': function() {
            // var num_pessoas = 6;
            // var ordem_morrer = 5;
            // var ordem_de_mortos = [5, 4, 6, 2, 3];
            // value_of(matar(num_pessoas, ordem_morrer)).should_be(ordem_de_mortos);
        // },
        '3 pessoas e posicao 5 a ser morto': function() {
            var num_pessoas = 3;
            var ordem_morrer = 5;
            var ordem_de_mortos = [2, 3];
            value_of(matar(num_pessoas, ordem_morrer)).should_be(ordem_de_mortos);
        },
        '6 pessoas e 5 passos até a vitima': function() {
            var pessoas = [1, 2, 3, 4, 5, 6];
            var passo = 5;
            var saida = [1, 2, 3, 4, 6];
            value_of(matar_proximo(pessoas, passo)).should_be(saida);
        },        
        '3 pessoas e 5 passos até a vitima': function() {
            var pessoas = 3;
            var passo = 5;
            var saida = [1,3];
            value_of(matar(pessoas, passo)).should_be(saida);
        }, 
        '2 pessoas e 1 passos até a vitima': function() {
            var num_pessoas = 2;
            var passo = 1;
            var saida = [1];
            value_of(matar(num_pessoas, passo)).should_be(saida);
        },         
    })
});
