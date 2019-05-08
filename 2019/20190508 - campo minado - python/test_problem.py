#!/usr/bin/env python
# -*- coding: utf-8 -*-

from problem import *


def test_campinho():
    campo = ['.']
    campo_pronto = ['0']
    assert campo_pronto == gera_campo(campo)