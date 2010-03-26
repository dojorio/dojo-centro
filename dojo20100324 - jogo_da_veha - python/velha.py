# -*- coding: utf-8 -*-
class Velha(object):

    def __init__(self, estatistica={}):
        self.estatistica = estatistica
        
    def proxima_jogada(self):
        dicionario = self.estatistica.values()
        if dicionario:
            return 2
        return 1
        
