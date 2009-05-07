import unittest
from estacionamento import *
from datetime import datetime

class TesteEstacionamentoNormal(unittest.TestCase):
    def setUp(self):
        carro = Carro("XYZ-1234")
        horario_entrada = datetime(2009, 5, 6, 19, 42)
        
        self.ticket = GeradorDeTicket().gerar(carro, horario_entrada)

    def teste_entra_e_sai_um_carro(self):
        horario_saida = datetime(2009, 5, 6, 20, 42)
        EncerradorDeTicket().encerrar(self.ticket, horario_saida)
        self.assertEqual(self.ticket.preco, 1)
        
    def teste_entra_e_sai_um_carro_gratis(self):
        horario_saida = datetime(2009, 5, 6, 20, 2)
        EncerradorDeTicket().encerrar(self.ticket, horario_saida)
        self.assertEqual(self.ticket.preco, 0)
        
        
    def teste_entra_e_sai_um_carro_duas_horas(self):
        horario_saida = datetime(2009, 5, 6, 21, 42)
        EncerradorDeTicket().encerrar(self.ticket, horario_saida)
        self.assertEqual(self.ticket.preco, 2)
    
if __name__ == '__main__':
    unittest.main()