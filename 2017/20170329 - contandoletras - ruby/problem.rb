def contaletras(valor)
	soma = 2

	if valor == 2
		soma += 4
		return soma 
	end

	if valor == 3
		soma += 4 + 4
		return soma
	end

	if valor == 4
		soma += 4 + 4 + 6
		return soma 
	end

	if valor == 5
		soma += 4 + 4 + 6 + 5
		return soma
	end 

	if valor == 6
		soma += 4 + 4 + 6 + 5 + 4
		return soma
	end 

    if valor == 7
    	soma += 4 + 4 + 6 + 5 + 4 + 4
		return soma
	end 

	if valor == 8
		soma += 4 + 4 + 6 + 5 + 4 + 4 + 4
		return soma
	end 

	if valor == 9
		soma += 4 + 4 + 6 + 5 + 4 + 4 + 4 + 4
		return soma
	end 

  	return soma
end