def contaletras(valor)
	lista = [
		"", "um", "dois", "tres", "quatro", "cinco",
		"seis", "sete", "oito", "nove", "dez", "onze",
		"doze", "treze", "quatorze", "quinze", "dezesseis", 
		"dezessete", "dezoito", "dezenove", "vinte",
		"vinte e um", "vinte e dois", "vinte e tres",
		"vinte e quatro", "vinte e cinco"
	]

	return lista[0..valor].join.gsub(" ", "").size
end