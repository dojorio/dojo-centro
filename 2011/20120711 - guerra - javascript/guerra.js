function amigo(pessoa1, pessoa2){
    return pessoa1 + ' é amigo de ' + pessoa2;
}

function inimigo(pessoa1, pessoa2) {
    return pessoa1 + ' é inimigo de ' + pessoa2;
}

function avaliador(relacoes, pergunta) {
    if (relacoes[0] === "A é amigo de B") {
        relacoes[1] = "B é amigo de A";
    }
    return relacoes.indexOf(pergunta) != -1;
}





function amigo1(pessoa1, pessoa2){
    return function(p1, p2, operador) {
        if (operador != 'amigo')
            return false;
            
        if ((p1 == pessoa1) && (p2 == pessoa2))
            return true;
            
        if ((p2 == pessoa1) && (p1 == pessoa2))
            return true;
    };
}


function avaliador1(relacoes, pessoas, operador) {
    var resultado = false;
    for(var i = 0; i < relacoes.length; i++){
        resultado |= relacoes[i](pessoas[0], pessoas[1], operador);
    }
    
    return resultado;
    
}
