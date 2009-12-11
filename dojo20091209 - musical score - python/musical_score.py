# -*- coding: utf-8 -*-

class Partitura(object):
    def __init__(self, partitura):
        self.linhas = partitura.split('\n')
        self.coluna = [linha[0] for linha in self.linhas]
        
    def qual_eh_nota(self):
        #coluna = [linha[0] for linha in self.linhas]
        notas = "FEDCBAGFE"
        posicao_da_nota = self.coluna.index('o') - 3
        return notas[posicao_da_nota]
        
    def qual_eh_duracao(self):
        if '|' in self.coluna:
            return 4
        return 1
        
    # def __repr__(self):
        # return self.qual_eh_nota() +'/'+ self.qual_eh_duracao()
