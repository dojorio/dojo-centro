def fizzbuzz(numero)
	if numero % 3 == 0
		return 'fizz'
	end

	if numero % 5 == 0 
		return 'buzz'
	end

	if numero % 3 == 0 && numero % 5 == 0  
		return 'fizzbuzz'
	end

		return numero
end