import unittest
from piratas import * 

class TestPiratas(unittest.TestCase):
    def test_dividir_uma_moeda_para_um_pirata_retorna_a_propria_moeda(this):
        moedas = [1]
        numero_de_piratas = 1
        piratas_moedas = dividir(moedas, numero_de_piratas)
        this.assertEquals(piratas_moedas, [[1]])

    def test_nao_posso_dividir_uma_moeda_para_dois_piratas(this):
        moedas = [1]
        numero_de_piratas = 2
        this.assertRaises(ValueError, dividir, moedas, numero_de_piratas)
        
    def test_dividir_moedas_iguais_para_dois_piratas(this):
        moedas = [1, 1]
        numero_de_piratas = 2
        piratas_moedas = dividir(moedas, numero_de_piratas)
        this.assertEquals(piratas_moedas, [[1], [1]])
    
    def test_nao_posso_dividir_moedas_cuja_soma_resulta_resto_diferente_0(this):
        moedas = [1, 2]
        numero_de_piratas = 2
        this.assertRaises(ValueError, dividir, moedas, numero_de_piratas)

    def test_nao_posso_dividir_moedas_cuja_soma_seja_maior_que_valor_medio_por_pirata(this):
        moedas = [1, 3]
        numero_de_piratas = 2
        this.assertRaises(ValueError, dividir, moedas, numero_de_piratas)

    def test_dividir_duas_moedas_para_um_pirata_retorna_o_proprio_conjunto_de_moedas(this):
        moedas = [1, 3]
        numero_de_piratas = 1
        piratas_moedas = dividir(moedas, numero_de_piratas)
        this.assertEquals(piratas_moedas, [[1, 3]])
        
unittest.main()
