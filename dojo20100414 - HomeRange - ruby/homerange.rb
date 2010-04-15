def homerange(lista_numerica)
	numeros = lista_numerica.split
	teste_seq = true
	numeros.size.times{ |i|
		if numeros[i + 1].to_i - numeros[i].to_i != 1
			teste_seq = false
		end
	}
	if teste_seq
		return numeros[0] + "-" + numeros[numeros.size -1] + "."
	end
	lista_numerica.gsub! " ", ", " 
	return lista_numerica + "."
end