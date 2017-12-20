exports.problem = function (numeros) {
	var soma = 0

	numeros.forEach(function(item, index, lista){
		soma += item.length
	}) 

    return soma
};
