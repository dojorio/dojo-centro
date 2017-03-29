def contaletras(valor)

	soma = 2

	if valor == 9
		return 2 + 4 + 4 + 6 + 5 + 4 + 4 + 4 + 4
	end 

	if valor == 8
		return 2 + 4 + 4 + 6 + 5 + 4 + 4 + 4
	end 

    if valor == 7
		return 2 + 4 + 4 + 6 + 5 + 4 + 4
	end 

	if valor == 6
		return 2 + 4 + 4 + 6 + 5 + 4
	end 
	if valor == 5
		return 2 + 4 + 4 + 6 + 5
	end 

	if valor == 4
		return 2 + 4 + 4 + 6
	end

	if valor == 3
		return soma + 4 + 4
	end

	if valor == 2
		soma += 4
		return soma 
	end

  	return soma
end