def busca(lista, busca)
	return [] if lista.values.empty?
	return [] if !lista.values[0].include?(busca)
	lista.keys
end
