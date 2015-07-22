def static verifica (texto) {
	def lista = texto.findAll{ it in ['c','a', 't']}

	lista.size() == 3 && lista == ['c', 'a', 't'] ? 'POSSIBLE':'IMPOSSIBLE'
}
