exports.troco = function (preco, pagamento) {
	var notas = [1, 2, 5]
	var troco = {}
	var nota = pagamento - preco

	if (nota > 0) {
		if (nota != 4 && notas.indexOf(nota)==-1){
			troco[5]=1
			troco[nota-5]=1
		} else {
			if (nota == 4) {
				troco[2] = 2
			} else {
				troco[nota] = 1
			}	
		}
		
	}

    return troco
};
