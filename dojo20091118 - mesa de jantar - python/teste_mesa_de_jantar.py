import unittest
from mesa_de_jantar import avaliar_disposicao

class TesteMesaDeJantar(unittest.TestCase):
    
    def test_0_relacao_eh_possivel(self):
        entrada = []
        self.assertEquals(True, avaliar_disposicao(entrada))  
        
    def test_2_convidados_1_relacao_eh_possivel(self):
        entrada = [("A", "B")]
        self.assertEquals(True, avaliar_disposicao(entrada))
        
    def test_3_convidados_2_relacoes_eh_possivel(self):
        entrada = [("A", "B"), ("A", "C")]
        self.assertEquals(True, avaliar_disposicao(entrada))      
      
    def test_3_convidados_3_relacoes_eh_impossivel(self):
        entrada = [("A", "B"), ("B", "C"), ("A", "C")]
        self.assertEquals(False, avaliar_disposicao(entrada)) 

    def test_3_convidados_1_relacoes_eh_possivel(self):
        entrada = [("A", "B")]
        self.assertEquals(True, avaliar_disposicao(entrada)) 

    def test_4_convidados_3_relacoes_eh_possivel(self):
        entrada = [("A", "B"), ("A", "C"), ("A", "D")]
        self.assertEquals(True, avaliar_disposicao(entrada)) 

    def test_4_convidados_4_relacoes_eh_impossivel(self):
        entrada = [("A", "B"), ("A", "C"), ("A", "D"), ("C", "D")]
        self.assertEquals(False, avaliar_disposicao(entrada))
    
    def test_4_convidados_3_relacoes_variado_eh_possivel(self):
        entrada = [("A", "B"), ("B", "C"), ("C", "D")]
        self.assertEquals(True, avaliar_disposicao(entrada))
        
if __name__ == '__main__':
    unittest.main()