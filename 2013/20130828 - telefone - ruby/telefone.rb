def matches(lista, busca)
	lista.select{ |nome, telefone| telefone.include?(busca) }
end
def busca(lista, busca)
	return [] if lista.values.empty?

	return matches(lista,busca).sort_by{|t| t[1].index(busca)}.map{|k,v| k}
end
