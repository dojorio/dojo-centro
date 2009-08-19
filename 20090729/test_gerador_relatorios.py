# -*- coding: utf-8 -*-
import unittest

# Relatórios
# Tipos: mensal, simplificado, anual
# Formatos: A4, Carta, A3
# Impressão: Colorido, P&B


from gerador_relatorios import *

class TestesDoGeradorDeRelatorio(unittest.TestCase):
	
	def teste_que_minha_impressora_imprime_um_relatorio_simplificado_em_a4_pb(self):
		relatorio_impresso = ImpressoraPb(
			FormatadorA4(
				GeradorDeRelatorioSimplificado()
			)
		)
		self.assertEqual(str(relatorio_impresso),
				'relatório simplificado <a4, pb>')
		
		def teste_que_minha_impressora_imprime_um_relatorio_simplificado_em_a4_colorido(self):
		relatorio = Relatorio()
		self.assertEqual(relatorio.imprimir('colorido'), u'relatório simplificado <a4, colorido>')

	"""		
	def teste_que_minha_impressora_imprime_um_relatorio_simplificado_em_a3_pb(self):
		relatorio = Relatorio()
		self.assertEqual(relatorio.imprimir(formato='a3'), u'relatório simplificado <a3, pb>')	
		
	def teste_que_minha_impressora_imprime_um_relatorio_simplificado_em_a3_colorido(self):
		relatorio = Relatorio()
		self.assertEqual(relatorio.imprimir('colorido', 'a3'), u'relatório simplificado <a3, colorido>')	
	"""
unittest.main()