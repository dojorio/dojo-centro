#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Balao:
    musica = [
        'cai', 'cai', 'mao',
        'nao', 'nao', 'nao', 'rua do sabao']

    def __init__(self):
        self.passos = []

    def cai_cai(self):
        self.passos.append('cai')

    def nao_cai_nao(self):
        self.passos.append('nao')

    def esta_ok(self):
        return self.passos == self.musica[:len(self.passos)]

    def na(self, onde):
        self.passos.append(onde)
