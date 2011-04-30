var telefone = function(texto) {
    for(var i=0; i<texto.length; i++){
    texto = texto.replace(/[ABC]/,'2');
    texto = texto.replace(/[DEF]/,'3');
    texto = texto.replace('J','5');
    texto = texto.replace('O','6');
    texto = texto.replace('Z','9');
   }

    return texto;
}
