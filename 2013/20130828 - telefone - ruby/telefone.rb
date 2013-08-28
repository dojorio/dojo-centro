def busca(lista, busca)
	return [] if busca == '1' && !lista.values[0].include?('1')
	lista.keys
end
