#!/usr/bin/env python
# -*- coding: utf-8 -*-


def time(value):
    cada_item = list(map(int, value.split(' ')))

    num_de_horas = cada_item[2] - cada_item[0]
    num_de_minutos = cada_item[3] - cada_item[1]

    if num_de_minutos < 0:
        num_de_minutos += 60
        num_de_horas -= 1




    
    return 'O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)'.format(num_de_horas, num_de_minutos)