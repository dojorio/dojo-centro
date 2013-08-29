def string_to_number(s)
	numbers = {
		'a' => 2,
		's' => 7
	}

	s.split('').map{ |c| numbers[c] || c }.join
end

def matches(lista, busca)
	lista.select do |nome, telefone|
		nome = string_to_number(nome.to_s)
		telefone.include?(busca) || nome.include?(busca)
	end
end

def sort_by_index(lista, busca)
	lista.sort_by do |contato|
		contato[1].index(busca).to_i +
		string_to_number(contato[0].to_s).index(busca).to_i
	end
end

def busca(lista, busca)
	return [] if lista.values.empty?

	sort_by_index(matches(lista,busca), busca).map{|k,v| k}
end
