function dependencias(diretas) {
    var transitivas = diretas;
    for(chave in diretas){
        diretas[chave].forEach(function (direta) {
            if (!diretas[direta]) {
                transitivas[direta] = [];
            } else {
                transitivas[chave] = transitivas[chave].concat(diretas[direta]);
            }
        });
        
    };
    return transitivas;
}
