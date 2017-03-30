def contaletras(valor)
	lista = [
		"", "um", "dois", "tres", "quatro", "cinco",
		"seis", "sete", "oito", "nove", "dez", "onze",
		"doze", "treze", "quatorze", "quinze", "dezesseis", 
		"dezessete", "dezoito", "dezenove", "vinte","vinteeum"
	]

	return lista[0..valor].join.size
end