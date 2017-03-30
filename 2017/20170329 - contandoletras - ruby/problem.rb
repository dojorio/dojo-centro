def contaletras(valor)
	lista = [
		"", "um", "dois", "tres", "quatro", "cinco",
		"seis", "sete", "oito", "nove", "dez", "onze"
	]

	return lista[0..valor].join.size
end