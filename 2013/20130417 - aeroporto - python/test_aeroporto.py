#-*- coding: utf-8 -*-
import unittest
from aeroporto import aeroporto

class AeroportoTestCase(unittest.TestCase):
    def test_vazio(self):
        patio = ['*']
        self.assertEqual(0, aeroporto(patio))

    def test_com_um_lugar(self):
        patio = ['* ']
        self.assertEqual(1, aeroporto(patio))

    def test_com_um_lugar_na_vertical(self):
        patio = [' ',
                 '*']
        self.assertEqual(1, aeroporto(patio))

    def test_com_um_bloqueio(self):
        patio = ['*#']
        self.assertEqual(0, aeroporto(patio))

    def test_com_um_bloqueio_e_um_espaco_antes_do_bloqueio(self):
        patio = ['* #']
        self.assertEqual(1, aeroporto(patio))

    def test_com_um_bloqueio_e_um_espaco_depois_do_bloqueio(self):
        patio = ['*# ']
        self.assertEqual(0, aeroporto(patio))

    def test_com_um_bloqueio_a_esquerda_da_entrada(self):
        patio = ['#* ']
        self.assertEqual(1, aeroporto(patio))

    def test_com_um_bloqueio_e_espaco_a_esquerda_da_entrada(self):
        patio = ['# *']
        self.assertEqual(1, aeroporto(patio))

    def test_com_bloqueios_dois_lados(self):
        patio = ['# * #']
        self.assertEqual(2, aeroporto(patio))

    def test_com_espacos_nos_extremos(self):
        patio = [' #*# ']
        self.assertEqual(0, aeroporto(patio))

    def test_com_bloqueio_espaco(self):
        patio = ['# #*# ']
        self.assertEqual(0, aeroporto(patio))

    def test_com_bloqueio_na_vertical_que_nao_atrapalha(self):
        patio = ['# ',
                 '* ']
        self.assertEqual(2, aeroporto(patio))

    def test_final_boss(self):
        patio = [' #  ',
                 '  # ',
                 '   #',
                 ' *  ']
        self.assertEqual(9, aeroporto(patio))

    def test_epic_boss(self):
        patio = ['    ',
                 '  # ',
                 '   #',
                 ' *  ']
        self.assertEqual(13, aeroporto(patio))

unittest.main()
