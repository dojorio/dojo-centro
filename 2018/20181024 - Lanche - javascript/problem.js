exports.problem = function (item, quantidade) {
	var tabela = {
		1: 4,
		2: 4.5,
		3: 5,
		4: 2,
		5: 1.5
	}

	if(tabela[item] == null || isNaN(parseInt(quantidade)) || quantidade < 0) {
		return 'Entrada Invalida'
	}

    return 'Total R$ ' + tabela[item] * quantidade
};
