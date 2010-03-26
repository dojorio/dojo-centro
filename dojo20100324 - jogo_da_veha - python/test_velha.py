# -*- coding: utf-8 -*-
import unittest
from velha import Velha

class TesteVelha(unittest.TestCase):
    
    def test_tabuleiro_vazio_e_sem_historico(self):
        velha = Velha()
        self.assertEquals(1, velha.proxima_jogada()) 
        
    def test_tabuleiro_com_algo_e_sem_historico(self):
        velha = Velha(['','','','','O','','','',''])
        self.assertEquals(1, velha.proxima_jogada()) 
        
    def test_tabuleiro_com_algo_e_com_historico_nulo(self):
        estado_do_tabuleiro = ('','','','','O','','','','')
        jogada = 1
        derrotas = 0
        empates = 0
        vitorias = 0
        estatistica_dos_jogos = {estado_do_tabuleiro: 
                                    {jogada: [derrotas, empates, vitorias]}
                                 }
        velha = Velha(estatistica_dos_jogos)
        self.assertEquals(1, velha.proxima_jogada()) 
        
    def test_tabuleiro_com_algo_e_com_historico(self):
        estado_do_tabuleiro = ('','','','','O','','','','')
        jogada = 2
        derrotas = 8
        empates = 0
        vitorias = 9
        estatistica_dos_jogos = {estado_do_tabuleiro: 
                                    {jogada: [derrotas, empates, vitorias]}
                                 }
        velha = Velha(estatistica_dos_jogos)
        self.assertEquals(2, velha.proxima_jogada())
        
        
    
unittest.main()