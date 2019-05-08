#!/usr/bin/env python
# -*- coding: utf-8 -*-

from problem import *


def test_campinho():
    campo = ['.']
    campo_pronto = ['0']
    assert campo_pronto == gera_campo(campo)

def test_campinho_com_bomba():
    campo = ['*']
    campo_pronto = ['*']
    assert campo_pronto == gera_campo(campo)

def test_campinho_2():
    campo = ['..']
    campo_pronto = ['00']
    assert campo_pronto == gera_campo(campo)
