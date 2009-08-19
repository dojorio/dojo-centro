# -*- coding: utf-8 -*-

class ImpressoraPb:
	cor = 'pb'
	def __init__(self, formatador):
		self.formatador = formatador
		
	def __repr__(self):
		return str(self.formatador) + self.cor + '>'
	
class FormatadorA4:
	tamanho = 'a4'

	def __init__(self, gerador_de_relatorio):
		self.gerador_de_relatorio = gerador_de_relatorio
	
	def __str__(self):
		return str(self.gerador_de_relatorio) + self.tamanho + ', '

class GeradorDeRelatorioSimplificado:
	tipo = 'relatório simplificado <'
	
	def __str__(self):
		return self.tipo
