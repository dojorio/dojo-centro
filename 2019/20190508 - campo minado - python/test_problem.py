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

def test_campinho_3():
    campo = ['...']
    campo_pronto = ['000']
    assert campo_pronto == gera_campo(campo)

def test_campinho_4():
    campo = ['*.']
    campo_pronto = ['*1']
    assert campo_pronto == gera_campo(campo)

def test_campinho_5():
    campo = ['.*']
    campo_pronto = ['1*']
    assert campo_pronto == gera_campo(campo)

def test_campinho_6():
    campo = ['*..']
    campo_pronto = ['*10']
    assert campo_pronto == gera_campo(campo)

def test_campinho_7():
    campo = ['*..*']
    campo_pronto = ['*11*']
    assert campo_pronto == gera_campo(campo)
