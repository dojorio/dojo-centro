
function ocupar(banheiro){
    var ultimo = banheiro.length -1;
    for(var posicao = ultimo; posicao>=0; posicao-=2)
        if (!banheiro[posicao])return posicao;
     return -1;
}