function paraIndoArabico(romano) {
    var romanos = {
        'I' : 1,
        'V' : 5, 
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    };
    var indoArabico = 0;
    var ultimo;
    romano.split().forEach(function(chave, valor){
       var atual = romano[chave];
       indoArabico = indoArabico + atual;
       
       if (atual > ultimo) {
            indoArabico = indoArabico - (2 * ultimo);
       }

       ultimo = atual;
    });
    
    }
    
    return indoArabico;
}