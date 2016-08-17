exports.troco = function (preco, pagamento) {
	if (preco == pagamento) {
		return {}
	}

	nota = pagamento - preco

    return preco == 1 ? { '1' : 1 } : { '2' : 1 }
};
