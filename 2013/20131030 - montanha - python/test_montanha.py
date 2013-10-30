import unittest
from montanha import escalar

class TestMontanha(unittest.TestCase):
    def test_nao_ha_escolha(self):
        montanha = [
            [1]
        ]
        self.assertEquals([1], escalar(montanha))

    def test_a_melhor_saida_eh_pela_direita(self):
        montanha = [
            [42, 1]
        ]
        self.assertEquals([2], escalar(montanha))

    def test_a_melhor_saida_eh_pela_esquerda(self):
        montanha = [
            [1, 42]
        ]
        self.assertEquals([1], escalar(montanha))

    def test_na_duvida_a_melhor_saida_ainda_eh_pela_esquerda(self):
        montanha = [
            [1, 1]
        ]
        self.assertEquals([1], escalar(montanha))

    def test_a_melhor_saida_eh_pela_extrema_direita(self):
        montanha = [
            [42, 42, 1]
        ]
        self.assertEquals([3], escalar(montanha))

    def test_a_melhor_saida_eh_pela_direita_nao_tao_extrema(self):
        montanha = [
            [42, 42, 1, 1]
        ]
        self.assertEquals([3], escalar(montanha))
    
    def test_a_melhor_saida_eh_pela_extrema_esquerda(self):
        montanha = [
            [1, 42, 1, 42]
        ]
        self.assertEquals([1], escalar(montanha))     

    def test_2_andares_unico_caminho(self):
        montanha = [
            [1],
            [2]
        ]
        self.assertEquals([1, 1], escalar(montanha))     

    def test_2_andares_caminho_diagonal(self):
        montanha = [
            [1, 2],
            [2, 1]
        ]
        self.assertEquals([2, 1], escalar(montanha))     

    def test_2_andares_sem_alcancar_o_menor_de_cima(self):
        montanha = [
            [1, 3, 2],
            [3, 3, 1]
        ]
        self.assertEquals([3, 3], escalar(montanha))     

    def test_2_onde_os_gulosos_nao_tem_vez(self):
        montanha = [
            [1, 42, 42],
            [3, 42,  1]
        ]
        self.assertEquals([1, 1], escalar(montanha))     


if __name__ == '__main__':
    unittest.main()
