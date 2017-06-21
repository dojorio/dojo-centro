#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Balao:
    desejadas = 0
    onde = ""
    secadas =0
    def cai_cai(self):
        self.desejadas += 1
        return True

    def nao_cai_nao(self):
        self.secadas +=1

    def esta_ok(self):
        return self.desejadas <= 2 and self.onde in  ("", "mão") and self.secadas <=3

    def na(self, onde):
        self.onde = onde
