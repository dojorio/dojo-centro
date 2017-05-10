def static roleta (pessoas, salto, inicio) {

	lista = [1..pessoas]

	while (lista.size() != 1) {
		if (inicio + salto > lista.size()) {
			inicio -= lista.size()
		}
		lista.remove(inicio + salto - 1)
		inicio = inicio + salto
	}

	'''if (pessoas in [3, 5, 8]) {
		return 3
	}
	 else if (pessoas in [6,9]){
	 	return 5
	 }'''
	return lista[0]
}
