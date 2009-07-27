# -*- coding: utf-8 -*-

def dividir(moedas, numero_de_piratas):
    soma_das_moedas = sum(moedas)
    maior_moeda = max(moedas)
    valor_por_pirata = soma_das_moedas / numero_de_piratas
    
    if soma_das_moedas % numero_de_piratas:
        raise ValueError(u"Não é possível dividir essas moedas para o número de piratas")
    elif maior_moeda > valor_por_pirata:
        raise ValueError(u"Moedão não cabe no bolso do pirata")

    if numero_de_piratas == 1:
        return [moedas]
    return [[moeda] for moeda in moedas]
