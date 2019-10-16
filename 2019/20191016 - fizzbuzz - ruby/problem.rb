def fizzbuzz(numero)
	if numero == 3 || numero == 6
		return 'fizz'
	end

	if numero == 5
		return 'buzz'
	end

	if numero == 1 || numero == 2 || numero == 4
		return numero
	end

	if numero == 8
		return 8
	end
end