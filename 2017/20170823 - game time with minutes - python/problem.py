#!/usr/bin/env python
# -*- coding: utf-8 -*-


def time(value):
    cada_item = list(map(int, value.split(' ')))

    num_de_horas = cada_item[2] - cada_item[0]
    num_de_minutos = cada_item[3] - cada_item[1]

    """if value == '1 1 2 1':
        num_de_horas = 1
    if value == '1 1 3 1':
        num_de_horas = 2

    num_de_minutos = int(value.split(' ')[3]) - 1 """
    
    return 'O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)'.format(num_de_horas, num_de_minutos)