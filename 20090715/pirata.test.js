$(function(){
module("Pirata");

test("Um pirata e nenhuma moeda", function(){
	var numeroDePiratas = 1;
	var moedas = [];
	equals(0, divide_moedas(numeroDePiratas, moedas));
});

test("Um pirata e uma moeda", function(){
	var numeroDePiratas = 1;
	var moeda = new Moeda(1);
	var moedas = [moeda];
	equals(1, divide_moedas(numeroDePiratas, moedas));
});

test("Dois piratas e duas moedas de valores iguais", function(){
	var numeroDePiratas = 2;
	var moeda1 = new Moeda(1);
	var moeda2 = new Moeda(1);
	var moedas = [moeda1, moeda2];
	isSet([moeda1,moeda2], divide_moedas(numeroDePiratas, moedas));
});

test("Dois piratas e três moedas de valores diferentes", function(){
	var numeroDePiratas = 2;
	var moeda1 = new Moeda(1);
	var moeda2 = new Moeda(2);
	var moeda3 = new Moeda(3);
	var moedas = [moeda1, moeda2, moeda3];
	isSet([moeda3],divide_moedas(numeroDePiratas, moedas)[0])
	isSet([moeda1, moeda2], divide_moedas(numeroDePiratas, moedas)[1]);
		
		
});

});
