import unittest
from anagramas import anagramas

class TesteAnagrama(unittest.TestCase):
    def teste_0_letra_deve_retornar_ela_mesma(self):
        self.assertEqual(anagramas(''), set(['']))

    def teste_1_letra_deve_retornar_ela_mesma(self):
        self.assertEqual(anagramas('a'), set(['a']))

    def teste_palavra_de_2_letras_iguais_tem_1_anagrama(self):
        self.assertEqual(anagramas('aa'), set(['aa']))
        
    def teste_palavra_de_2_letras_diferentes_tem_2_anagramas(self):
        self.assertEqual(anagramas('ab'), set(['ab','ba']))
       
    def teste_palavra_ca_tem_os_anagramas_ca_e_ac(self):
        self.assertEqual(anagramas('ca'), set(['ca','ac']))
        
    def teste_palavra_3_letras_iguais_tem_1_anagrama(self):
        self.assertEqual(anagramas('aaa'), set(['aaa']))
        
    def teste_palavra_3_letras_diferentes_tem_6_anagrama(self):
        self.assertEqual(anagramas('abc'), set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        
    def teste_biro(self):
        self.assertEqual(anagramas('biro'),
            set('''biro bior brio broi boir bori
                    ibro ibor irbo irob iobr iorb
                    rbio rboi ribo riob roib robi
                    obir obri oibr oirb orbi orib'''.split()))
        
unittest.main()