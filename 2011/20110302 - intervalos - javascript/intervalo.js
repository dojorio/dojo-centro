var ListaDeIntervalos = function() {
	this.vetor = [];
	this.ultimo_inserido = undefined;

	this.inserir_em_novo = function(numero) {
		this.vetor.push([numero]);
		this.ultimo_inserido = numero;
	};

	this.inserir_no_ultimo = function(numero) {
		this.vetor[vetor.length - 1][1] = numero;
		this.ultimo_inserido = numero;
	};

	this.ultimo_vem_antes_de = function(numero) {
		return this.ultimo_inserido-numero == 1;
	}
};

function intervalo(numeros) {
	var saida = new ListaDeIntervalos();

	numeros.sort();

	numeros.forEach(function(numero, i) {
		if (saida.ultimo_vem_antes_de(numero))
			saida.inserir_no_ultimo(numero);
		else		
			saida.inserir_em_novo(numero);
	})	
	
	return saida.vetor;
}
