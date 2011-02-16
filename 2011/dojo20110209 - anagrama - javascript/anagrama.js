function anagrama(palavra){
    anagramas = [palavra]
    if( palavra.length> 1 && (palavra[0]!= palavra[1])){
        anagramas.push(revertePalavra(palavra))
        if (palavra.length == 3){
            prim_let = palavra[0]
            meio_let = palavra[1]
            anagramas.push((prim_let+meio_let+prim_let))
            
        }
    }
    //removerPalavrasRepetidas(anagramas)
    return anagramas.sort()
}

function revertePalavra(palavra){
    return palavra.split('').reverse().join('')
}

function removerPalavrasRepetidas(anagramas){
    anagramas = anagramas.sort()
    //for(i=1; )
}
