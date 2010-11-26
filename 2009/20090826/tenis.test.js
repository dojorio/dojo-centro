$(function(){
module("Tenis");

test("Jogador A fez ponto quando o placar estava 15, 30", function(){
	var placarAtual = {A: 15, B: 30};
	var pontuador = "A";
	equals(AtualizarPlacar(placarAtual, pontuador), "30, 30");
});

test("Jogador B fez ponto quando o placar estava 15, 15", function(){
	var placarAtual = {A: 15, B: 15};
	var pontuador = "B";
	equals(AtualizarPlacar(placarAtual, pontuador), "15, 30");
});

test("Jogador A fez ponto quando o placar estava 0, 0", function(){
	var placarAtual = {A: 0, B: 0};
	var pontuador = "A";
	equals(AtualizarPlacar(placarAtual, pontuador), "15, 0");
});

test("Jogador B fez ponto quando o placar estava 0, 0", function(){
	var placarAtual = {A: 0, B: 0};
	var pontuador = "B";
	equals(AtualizarPlacar(placarAtual, pontuador), "0, 15");
});

test("Jogador A fez ponto quando o placar estava 15, 15", function(){
	var placarAtual = {A: 15, B: 15};
	var pontuador = "A";
	equals(AtualizarPlacar(placarAtual, pontuador), "30, 15");
});

test("Jogador B fez ponto quando o placar estava 30, 15", function(){
	var placarAtual = {A: 30, B: 15};
	var pontuador = "B";
	equals(AtualizarPlacar(placarAtual, pontuador), "30, 30");
});

test("Jogador B fez ponto quando o placar estava 15, 30", function(){
	var placarAtual = {A: 15, B: 30};
	var pontuador = "B";
	equals(AtualizarPlacar(placarAtual, pontuador), "15, 40");
});

test("Jogador B fez ponto quando o placar estava 30, 15", function(){
	var placarAtual = {A: 30, B: 15};
	var pontuador = "A";
	equals(AtualizarPlacar(placarAtual, pontuador), "40, 15");
});
});
