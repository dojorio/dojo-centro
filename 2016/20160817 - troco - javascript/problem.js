exports.troco = function (preco, pagamento) {
	var troco = {}
	if (preco == pagamento) {
		return troco
	}

	var nota = pagamento - preco
	

	troco [nota]=1
    return troco
};
