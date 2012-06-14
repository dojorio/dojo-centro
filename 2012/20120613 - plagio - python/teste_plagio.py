#coding:utf-8
import unittest, plagio


class TestTokenizar(unittest.TestCase):    
    def teste_tokenizacao(self):
        texto = 'ola tudo bem'
        self.assertEqual(['ola', 'tudo', 'bem'], plagio.tokenizar(texto))
        
    def teste_com_pontuacao(self):
        texto = 'ola, tudo bem?'
        self.assertEqual(['ola', 'tudo', 'bem'], plagio.tokenizar(texto))
    
    def teste_com_maiusculas(self):
        texto = 'Ola, tudo bem?'
        self.assertEqual(['Ola', 'tudo', 'bem'], plagio.tokenizar(texto))
    
    def teste_com_acento(self):
        texto = u'olá, tudo bem? ação'
        self.assertEqual([u'olá', 'tudo', 'bem', u'ação'], 
                         plagio.tokenizar(texto))
        
    def teste_com_acento_o(self):
        texto = u'olá, tudo bem? ação orações'
        self.assertEqual([u'olá', u'tudo', u'bem', u'ação', u'orações'],
                         plagio.tokenizar(texto))
         
    def teste_string_vazia(self):
        texto = ''
        self.assertEqual([], plagio.tokenizar(texto))

class TestDistancia(unittest.TestCase):
    def teste_textos_iguais(self):
        texto1 = u'olá, tudo bem?'
        texto2 = texto1
        self.assertEqual(0, plagio.distancia(texto1, texto2)) 

    def teste_textos_iguais_exceto_pela_pontuacao(self):
        texto1 = u'olá, tudo bem?'
        texto2 = u'olá tudo bem'
        self.assertEqual(0, plagio.distancia(texto1, texto2)) 

class TestDistanciaTextosDiferentes(unittest.TestCase):
    def teste_uma_palavra(self):
        texto1 = 'aperte o play?'
        texto2 = 'aperte o'
        self.assertEqual(1, plagio.distancia(texto1, texto2)) 

    def teste_uma_palavra_com_o_segundo_texto_maior(self):
        texto1 = 'aperte o'
        texto2 = 'aperte o play?'
        self.assertEqual(1, plagio.distancia(texto1, texto2)) 
        
    def teste_por_uma_troca_insercao(self):
        texto1 = 'aperte a'
        texto2 = 'aperte o play?'
        self.assertEqual(2, plagio.distancia(texto1, texto2)) 
        
    def teste_por_uma_troca_delecao(self):
        texto1 = 'aperte o play?'
        texto2 = 'aperte a'
        self.assertEqual(2, plagio.distancia(texto1, texto2)) 
        
    def teste_por_uma_troca(self):
        texto1 = 'aperte a play'
        texto2 = 'aperte o play?'
        self.assertEqual(1, plagio.distancia(texto1, texto2)) 
        
    def teste_por_uma_delecao_no_comeco(self):
        texto1 = 'aperte o play'
        texto2 = 'o play'
        self.assertEqual(1, plagio.distancia(texto1, texto2)) 
    
        
unittest.main()


