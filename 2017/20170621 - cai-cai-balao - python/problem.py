#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Balao:
    desejadas = 0
    onde = ""

    def cair(self):
        self.desejadas += 1
        return True

    def esta_ok(self):
        self.desejadas <= 2 and self.onde == "mão"

    def na(self, onde):
        if onde == "mão":
            self.onde = onde
