def static roleta (pessoas, salto, inicio) {

	def lista = 1..pessoas
    lista = lista.toList()

	while (lista.size() != 1) {
		while (inicio + salto > lista.size()) {
			inicio -= lista.size()
		}
		
		lista.remove(inicio + salto - 1)
		inicio = inicio + salto
	}

	return lista[0]
}
