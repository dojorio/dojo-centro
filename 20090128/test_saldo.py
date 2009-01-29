import unittest
from saldo import Partidas, Partida

class TesteSaldo(unittest.TestCase):
    def teste_uma_vitoria(self):
        partidas = Partidas([Partida(1, 0)]) # uma unica partida com resultado 1 x 0
        #self.assertEqual(partidas.melhor_saldo(), (1, 1))
        
    #def teste_uma_derrota(self):
     #   partidas = Partidas([Partidas(0, 1)])
        #self.assertEqual(partidas.melhor_saldo(), "nenhum")
        
unittest.main()
