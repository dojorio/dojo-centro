#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/en/problems/view/1047

def time(value):
    itens = list(map(int, value.split(' ')))
    horas = itens[2] - itens[0]
    minutos = itens[3] - itens[1]

    if minutos < 0:
        minutos += 60
        horas -= 1
    if horas == 0 == minutos:
        horas = 24
    if horas < 0:
        horas += 24

    plural_horas = ''
    if horas > 1:
        plural_horas = 'S'
    
    plural_minutos = ''
    if minutos > 1:
        plural_minutos = 'S'

    return 'O JOGO DUROU {0} HORA{1} E {2} MINUTO{3}'.format(horas, plural_horas, minutos, plural_minutos)