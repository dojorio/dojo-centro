def string_to_number(s)
	numbers = {
		'a' => 2,
		's' => 7
	}

	s.split('').map{ |c| numbers[c] }.join
end

def matches(lista, busca)
	lista.select do |nome, telefone|
		nome = string_to_number(nome.to_s)
		telefone.include?(busca) || nome.include?(busca)
	end
end

def sort_by_index(lista, busca)
	lista.sort_by { |contato| contato[1].index(busca) }
	lista.sort_by { |contato| string_to_number(contato[0]).index(busca) }
end

def busca(lista, busca)
	return [] if lista.values.empty?

	sort_by_index(matches(lista,busca), busca).map{|k,v| k}
end
