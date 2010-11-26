var Moeda = function(valor) {
	this.valor = valor;
}

function divide_moedas(numeroDePiratas, moedas) {
	if(numeroDePiratas > 1){
		if (moedas.length == 3){
			
			return [[moedas[2]], [moedas[0],moedas[1]]];
		}else{
			return moedas;
		}
	}
	return moedas.length;
};