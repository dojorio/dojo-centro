exports.troco = function (preco, pagamento) {
	var notas = [1, 2, 5]
	var troco = {}
	var valor_troco = pagamento - preco

	if (valor_troco > 0) {
		if (notas.indexOf(valor_troco) == -1) {
			if (valor_troco > 5) {
				troco[5] = 1
				var diff5 = valor_troco - 5
				if (notas.indexOf(diff5) == -1) {
					if (diff5 == 3) {
						troco[2] = 1
						troco[1] = 1	
					} else {
						troco[2] = 2
					}
				} else {
					troco[diff5] = 1
				}	
			} else {
				troco[2] = 2
			}
		} else {
			troco[valor_troco] = 1
		}
	}

    return troco
};
