function matar(num_pessoas, passo) {
    if ( num_pessoas ==  1 ) {
        return []
    }
    var pessoas = [];
    
    for( var i = 1; i <= num_pessoas; i++ ) {
        pessoas.push(i);
    }
    return matar_proximo({mortos:[], vivos:pessoas, passo:passo});
    
}   

function matar_proximo(parametro){
    var pessoa_a_matar = parametro.passo % parametro.vivos.length;
    var indice_da_pessoa_que_vai_morrer = pessoa_a_matar - 1;
    parametro.vivos.splice(indice_da_pessoa_que_vai_morrer, 1);
    
    return parametro.vivos;
}
