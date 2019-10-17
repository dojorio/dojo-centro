def fizzbuzz(numero)
	if numero == 3 || numero == 6 || numero == 9
		return 'fizz'
	end

	if numero == 5
		return 'buzz'
	end

	if numero == 1 || numero == 2 || numero == 4 || numero == 7 || numero == 8
		return numero
	end

end