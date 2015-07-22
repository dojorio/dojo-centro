def static verifica (texto) {
	lista = texto.findAll{it in ['c','a', 't']}

	lista.size() == 3  ? 'POSSIBLE':'IMPOSSIBLE'
}
