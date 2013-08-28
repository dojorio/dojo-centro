def busca(lista, busca)
	return [] if lista.values.empty?

	return lista.select{ |nome, telefone| telefone.include?(busca) }.sort_by{|t| t[1].index(busca)}.map{|k,v| k}
end
