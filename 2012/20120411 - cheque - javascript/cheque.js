
var numerosExtensos = {
	0: "zero",
	1: "um",
	2: "dois",
	3: "três",
	4: "quatro",
	5: "cinco",
	6: "seis",
	7: "sete",
	8: "oito",
	9: "nove",
	
	10: "dez",
	11: "onze",
	12: "doze",
	13: "treze",
	14: "quatorze",
	15: "quinze",	
	16: "dezesseis",
	17: "dezessete",
	18: "dezoito",
	19: "dezenove",
	
	20: "vinte",
	30: "trinta",
	40: "quarenta",
	50: "cinquenta",
	60: "sessenta",
	70: "setenta",
	80: "oitenta",
	90: "noventa",
	
	100: "cem",
	200: "duzentos",
	300: "trezentos",
	400: "quatrocentos",
	500: "quinhentos",
	600: "seiscentos",
	700: "setecentos",
	800: "oitocentos",
	900: "novecentos",
}

function numeroPosicionalPorExtenso(numero) {
	var resultado = [];
	
	numero = "" + numero;
	
	for (var i = numero.length-1; i >= 0; i--) {
		var x = numero[i] * Math.pow(10, i);
		resultado.unshift(numerosExtensos[x]);
	}
	
	console.log(resultado);
	
	return resultado.join(" e ");
}

function numeroPorExtenso(numero) {
	var milhares, centenas, dezenas, unidades, resto;
	
	if (numero < 100) {
		return numeroPosicionalPorExtenso(numero);
	}
	
	if (numerosExtensos[numero]) {
	    return numerosExtensos[numero];
	    
	} else if (numero < 100) {
		dezenas = Math.floor(numero / 10);
		unidades = numero % 10;
		return numeroPorExtenso(dezenas * 10) + " e " + numeroPorExtenso(unidades);
		
	} else if (numero < 1000) {
		centenas = Math.floor(numero / 100);
		resto = numero - (centenas * 100);
		
		if (centenas == 1) {
			return "cento e " + numeroPorExtenso(resto);
		} else {
			return numeroPorExtenso(centenas * 100) + " e " + numeroPorExtenso(resto);
		}
	} else {
		milhares = Math.floor(numero / 1000);
		resto = numero - milhares * 1000;
		if (resto == 0)
			return numeroPorExtenso(milhares) + " mil";
			
		return numeroPorExtenso(milhares) + " mil" + " e " + numeroPorExtenso(resto);
	}
}

