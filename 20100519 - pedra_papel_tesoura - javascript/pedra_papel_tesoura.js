Jogador = function(nome, jogada){
    this.nome = nome;
    this.jogada = jogada;
}
function ganha(jogada1,jogada2){
    if jogada1 =='tesoura'
        return true
}

function ganhador(jogador1, jogador2){
    if (jogador1.jogada.ganha(jogador2.jogada))
        return jogador1.nome
    else
        return jogador2.nome
}

function jokenpo(jogadores) {

    this.todosIguais = function(){

        if(jogadores[0].jogada == jogadores[1].jogada){
            return true;
        }

    }


    if(jogadores.length == 1)
        return [jogadores[0].nome];
     else
        if (this.todosIguais()){
            return [jogadores[0].nome, jogadores[1].nome];
        }
        if (jogadores[0].jogada == "tesoura" &&
         jogadores[1].jogada == "papel") {
            return [jogadores[0].nome];
        }
        else if (jogadores[0].jogada== "papel" &&
        jogadores[1].jogada== "pedra"){
            return [jogadores[0].nome];
        }
        else{
            return [jogadores[1].nome];
        }
}

