def contaletras(valor)
	lista = [
		"zero", "um", "dois", "tres", "quatro", "cinco",
		"seis", "sete", "oito", "nove", "dez", "onze"
	]

	soma = 2

	if valor >= 2
		soma += 4
	end

	if valor >= 3
		soma += 4
	end

	if valor >= 4
		soma += 6
	end

	if valor >= 5
		soma += 5
	end 

	if valor >= 6
		soma += 4
	end 

    if valor >= 7
    	soma += 4
	end 

	if valor >= 8
		soma += 4
	end 

	if valor >= 9
		soma += 4
	end 

	if valor >= 10
		soma += 3
	end 

	if valor >= 11
		soma += 4
	end 

  	return soma
end