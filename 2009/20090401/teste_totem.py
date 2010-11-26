import unittest

from totem import achar_assinatura
from textwrap import dedent

class TesteTotem(unittest.TestCase):
    def teste_1x1_igual(self):
        totem = "_"
        parte = "_"
        coordenadas = achar_assinatura(totem, parte)
        self.assertEqual(coordenadas, [(0, 0)])
        
    def teste_1x1_diferente(self):
        totem = "_"
        parte = "|"
        coordenadas = achar_assinatura(totem, parte)
        self.assertEqual(coordenadas, [])
        
    def teste_2x1(self):
        totem = dedent("""\
                        _|
                        _|""")
                
        parte = "|"
        coordenadas = achar_assinatura(totem, parte)
        self.assertEqual(coordenadas, [(0, 1),(1, 1)])
        
    def teste_2x2(self):
        totem = dedent("""\
                        _|
                        _|""")
                
        parte = dedent("""\
                        _|
                        _|""")
        coordenadas = achar_assinatura(totem, parte)
        self.assertEqual(coordenadas, [(0, 0)])
    
    def teste_1x2(self):
        totem = "_"
        parte = dedent("""\
                        _|
                        _|""")
        coordenadas = achar_assinatura(totem, parte)
        self.assertEqual(coordenadas, [])
        
        
unittest.main()        
