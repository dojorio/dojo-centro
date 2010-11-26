#!/usr/bin/env python
# -*- coding: utf-8 -*-


def espiral(linha, coluna):
    maximo = linha * coluna
    tamanho_do_item = len(str(maximo))

    def processa_item(item):
        return str(item).rjust(tamanho_do_item, " ")

    primeira_linha = " ".join(map(processa_item, range(1, coluna + 1)))
    segunda_linha = " ".join(map(processa_item, range(maximo, coluna, -1)))

    return "\n".join((primeira_linha, segunda_linha)).rstrip()

