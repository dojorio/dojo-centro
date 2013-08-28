def busca(lista, busca)
	return [] if lista.values.empty?

	return lista.select{ |nome, telefone| telefone.include?(busca) }.map{|k,v| k}
end
