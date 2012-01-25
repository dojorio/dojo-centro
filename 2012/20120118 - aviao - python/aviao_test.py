import unittest

import aviao

class TesteAviaoCom2Passageiros(unittest.TestCase):
    def testa_embarca_dois_passageiros(self):
        embarcados = aviao.embarcar(2)
        # quantidade_dos_passageiros
        self.assertEqual(len(embarcados), 2)
        # os_passageiros_entraram_no_aviao
        self.assertTrue(1 in embarcados and 2 in embarcados)
    
    def testa_probabilidade_de_50_por_cento(self):
        contador = 0
        
        for i in range(42000):
            ultimo_passageiro = aviao.embarcar(2)[-1]
            if ultimo_passageiro == 2:
                contador += 1
                
        self.assertTrue(20500 < contador < 21500, contador)
        
        
class TesteAviaoCom3Passageiros(unittest.TestCase):
    def testa_embarca_tres_passageiros(self):
        embarcados = aviao.embarcar(3)
        self.assertEqual(len(embarcados),3)
        self.assertTrue(1 in embarcados and 2 in embarcados
                        and 3 in embarcados) 
       
    def testa_probabilidade_de_50_por_cento(self):
        contador = 0
        
        for i in range(42000):
            ultimo_passageiro = aviao.embarcar(3)[-1]
            if ultimo_passageiro == 3:
                contador += 1
                
        self.assertTrue(20500 < contador < 21500, contador)
   
class TesteAviaoCom100Passageiros(unittest.TestCase):
    def testa_embarca_tres_passageiros(self):
        embarcados = aviao.embarcar(100)
        self.assertEqual(len(embarcados), 100)
        #self.assertTrue(1 in embarcados and 2 in embarcados
                        #and 3 in embarcados) 
       
    def testa_probabilidade_de_50_por_cento(self):
        contador = 0
        
        for i in range(42000):
            ultimo_passageiro = aviao.embarcar(100)[-1]
            if ultimo_passageiro == 100:
                contador += 1
                
        self.assertTrue(20500 < contador < 21500, contador)  
       
if __name__ == '__main__':
    unittest.main()

