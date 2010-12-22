var Jogada = function(valor) {
	this.valor = valor;

	var regraDeVencedores = { 
		'tesoura': 'papel', 
		'papel': 'pedra',
		'pedra': 'tesoura'
	};

	this.ganhaDe = function(outraJogada) {
		return regraDeVencedores[this.valor] == outraJogada.valor;
	}
};

var jokenpo = function(valorDaJogada1, valorDaJogada2){
	var jogada1 = new Jogada(valorDaJogada1);
	var jogada2 = new Jogada(valorDaJogada2);

	if (jogada1.ganhaDe(jogada2)) return jogada1.valor;
	if (jogada2.ganhaDe(jogada1)) return jogada2.valor;

	return 'empate';

}

