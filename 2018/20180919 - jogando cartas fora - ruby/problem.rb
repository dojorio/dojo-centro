def cartasfora(cartas)
	pilha = []
	count = 1

	cartas.times do
	  pilha << count
	  count += 1
	end

	descartes = []

	while pilha.size > 1
		topo = pilha.shift
		descartes << topo
		topo = pilha.shift
		pilha << topo
	end

	return [descartes, pilha[0]]


end