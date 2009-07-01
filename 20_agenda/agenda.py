class Agenda:
	
	eventos = []
	
	def colide(self, outra_agenda):		
		if len(self.eventos) > 0:
			return True
		else:
			return False
			
		
	def adicionar(self, evento):
		self.eventos.append(evento)
		
class Evento:
	def __init__(self, nome, inicio, fim):
		pass