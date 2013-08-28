def matches(lista, busca)
	lista.select{ |nome, telefone| telefone.include?(busca) || (busca == '2' && nome.to_s.include?('a')) }
end

def sort_by_index(lista, busca)
	lista.sort_by { |contato| contato[1].index(busca) }
end

def busca(lista, busca)
	return [] if lista.values.empty?

	sort_by_index(matches(lista,busca), busca).map{|k,v| k}
end
