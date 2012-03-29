import unittest
from eval import avaliar


class TestEval(unittest.TestCase):
    def test_avaliar_constante_0(self):
        expressao = "0"
        self.assertEqual(avaliar(expressao), 0)
        
    def test_avaliar_constante(self):
        expressao = "2"
        self.assertEqual(avaliar(expressao), 2)
        
    def test_avaliar_constante_mais_algarismos(self):
        expressao = "2312732"
        self.assertEqual(avaliar(expressao), 2312732)
        
    def test_avaliar_negativo(self):
        expressao = "-1"
        self.assertEqual(avaliar(expressao), -1)
        
    def test_avaliar_constante_operador_constante(self):
        expressao = "1*1"
        self.assertEqual(avaliar(expressao), 1)
        
    def test_avaliar_constante_tamanho_3(self):
        expressao = "111"
        self.assertEqual(avaliar(expressao), 111)
        
    def test_avaliar_dois_vezes_um(self):
        expressao = "2*1"
        self.assertEqual(avaliar(expressao), 2)
        
    def test_avaliar_dois_vezes_tres(self):
        expressao = "2*3"
        self.assertEqual(avaliar(expressao), 6)
        
    def teste_avaliar_dez_vezes_dois(self):
        expressao = "10*2"
        self.assertEqual(avaliar(expressao), 20)
        
    def teste_avaliar_dois_vezes_dez(self):
        expressao = "2*10"
        self.assertEqual(avaliar(expressao), 20)
    
    def teste_avaliar_dois_vezes_dez_vezes_dois(self):
        expressao = "2*10*2"
        self.assertEqual(avaliar(expressao), 40)
    
    def teste_avaliar_dois_mais_dois(self):
        expressao = "2+2"
        self.assertEqual(avaliar(expressao), 4)

    def teste_avaliar_dois_menos_dois(self):
        expressao = "2-2"
        self.assertEqual(avaliar(expressao), 0)
    
    def teste_avaliar_menos_dois_menos_dois(self):
        expressao = "-2-2"
        self.assertEqual(avaliar(expressao), -4)
    
    def teste_avaliar_menos_dois_mais_dois(self):
        expressao = "-2+2"
        self.assertEqual(avaliar(expressao), 0)
    
    def teste_avaliar_mais_dois_menos_dois(self):
        expressao = "+2-2"
        self.assertEqual(avaliar(expressao), 0)
        
    def teste_avaliar_expressao_grande_mista(self):
        expressao = "-3*2-3+2-2"
        self.assertEqual(avaliar(expressao), -9)
        
    def teste_avaliar_expressao_com_precedencia(self):
        expressao = "1-2*2"
        self.assertEqual(avaliar(expressao), 2)
    
        
unittest.main()
