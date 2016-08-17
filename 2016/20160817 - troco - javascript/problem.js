exports.troco = function (preco, pagamento) {
	var notas = [1, 2, 5]
	var troco = {}
	var valor_troco = pagamento - preco

	if (valor_troco > 0) {
		if (notas.indexOf(valor_troco) == -1) {
			if (valor_troco > 5) {
				troco[5] = 1
				troco[valor_troco - 5] = 1
			} else {
				troco[2] = 2
			}
		} else {
			troco[valor_troco] = 1
		}
	}

    return troco
};
