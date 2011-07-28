function AtualizarPlacar (placarAtual, pontuador) {
	if (pontuador == "A" ) {
		if (placarAtual.A >= 30){
			placarAtual.A += 10;
		} else {
			placarAtual.A += 15;
		}
		return placarAtual.A + ", " + placarAtual.B;
	}
	if (pontuador == "B" ) {
		if (placarAtual.B >= 30){
			placarAtual.B += 10;
		} else {
			placarAtual.B += 15;
		}
		return placarAtual.A + ", " + placarAtual.B;
	}
};