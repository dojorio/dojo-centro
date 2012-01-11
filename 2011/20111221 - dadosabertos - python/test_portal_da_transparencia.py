# coding:utf-8
import unittest, portal_da_transparencia as p


class PortalDaTransparencia_Municipios(unittest.TestCase):
    def test_soma_valores_de_um_municipio(self):
        dados = [{"Nome Município": "ARMACAO DE BUZIOS", "Valor": 1936.97}]
        esperado = {
            "ARMACAO DE BUZIOS": 1936.97
        }
        self.assertEqual(esperado, p.agrupar(dados))

    def test_soma_de_varios_valores_de_um_mesmo_municipio(self):
        dados = [{"Nome Município": "ARMACAO DE BUZIOS", "Valor": 1},
        {"Nome Município": "ARMACAO DE BUZIOS", "Valor": 2}]        
        esperado = {
            "ARMACAO DE BUZIOS": 3
        }
        self.assertEqual(esperado, p.agrupar(dados))
        
    def test_soma_de_varios_valores_de_dois_municipios(self):
        dados = [
            {"Nome Município": "ARMACAO DE BUZIOS", "Valor": 1},
            {"Nome Município": "ARMACAO DE BUZIOS", "Valor": 2},
            {"Nome Município": "MACUCO", "Valor": 3}
        ]
        esperado = {
            "ARMACAO DE BUZIOS": 3,
            "MACUCO": 3
        }
        
        self.assertEqual(esperado, p.agrupar(dados))
        
    def test_soma_de_tres_valores_de_um_municipio(self):
        dados = [
            {"Nome Município": "ARMACAO DE BUZIOS", "Valor": 1},
            {"Nome Município": "ARMACAO DE BUZIOS", "Valor": 2},
            {"Nome Município": "ARMACAO DE BUZIOS", "Valor": 5},
        ]
        esperado = {"ARMACAO DE BUZIOS": 8}
            
        self.assertEqual(esperado, p.agrupar(dados))

class PortalDaTransparencia_Funcoes(unittest.TestCase):
    def test_soma_valores_de_uma_funcao(self):
        dados = [
            {
                "Nome Município": "ARMACAO DE BUZIOS",
                "Nome Função": "Saúde",
                "Valor": 1
            }
        ]
        esperado = {
            "Saúde": 1
        }
        self.assertEqual(esperado, p.agrupar(dados, "Nome Função"))
    
        
        
if __name__ == '__main__':
    unittest.main()