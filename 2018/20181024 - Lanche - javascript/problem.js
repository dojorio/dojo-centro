exports.problem = function (item, quantidade) {
	var tabela = {
		1: 4,
		2: 4.5,
		3: 5,
		4: 2,
		5: 1.5
	}
	
    return tabela[item] * quantidade
};
