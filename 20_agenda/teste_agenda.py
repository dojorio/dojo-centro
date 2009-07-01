import unittest
from agenda import Agenda, Evento
from datetime import datetime

class AgendaTeste(unittest.TestCase):
	def teste_colisao_agendas_vazias(self):
		agenda1 = Agenda()
		agenda2 = Agenda()
		
		self.assertFalse(agenda1.colide(agenda2))
	
	def teste_colisao_agendas_um_evento_cada(self):	
		futebol = Evento(
			nome="Futebol",
			inicio=datetime(2009,1,1,0,0,0),
			fim=datetime(2009,1,1,1,0,0)
			)
		agenda1 = Agenda()
		agenda1.adicionar(futebol)
		agenda2 = Agenda()
		agenda2.adicionar(futebol)
		
		self.assertTrue(agenda1.colide(agenda2))

		
if __name__ == '__main__':
	unittest.main()