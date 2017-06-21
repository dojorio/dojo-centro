#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Balao:
    desejadas = 0
    onde = ""
    indesejadas =0

    passos = []
    musica = ['cai', 'cai', 'mao', 'nao', 'nao', 'nao']

    def cai_cai(self):
        self.passos.append('cai')
        return True

    def nao_cai_nao(self):
        self.passos.append('nao')
        self.indesejadas +=1
        if self.onde == '':
            self.indesejadas = 99

    def esta_ok(self):
        #return self.desejadas <= 2 and self.onde in  ("", "mao") and self.indesejadas <=3
        return self.passos == self.musica[:len(self.passos)]

    def na(self, onde):
        self.passos.append(onde)
        self.onde = onde
