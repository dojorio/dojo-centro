def busca(lista, busca)
	return [] if lista.values.empty? || !lista.values[0].include?(busca)
	lista.keys
end
