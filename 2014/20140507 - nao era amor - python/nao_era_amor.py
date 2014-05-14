MULTIPLICADORES = {
  '+': 1,
  '-': -1,
  '.': 0
}

def aplica_padrao(linha, padrão):
    resultado = 0
    for numero, operador in zip(linha, padrão):
        resultado += numero * MULTIPLICADORES[operador]
    return resultado

def cilada(tabuleiro, padrões):
    resultados_possiveis = []
    último_padrão = None

    for linha in tabuleiro:
        resultados_linha = []
        for padrão in padrões:
            if padrão != último_padrão:
                resultado = aplica_padrao(linha, padrão)
                resultados_linha.append(resultado)
            else:
                resultados_linha.append(0)

        melhor_da_linha = max(resultados_linha)
        indice = resultados_linha.index(melhor_da_linha)
        último_padrão = padrões[indice]
        resultados_possiveis.append(melhor_da_linha)


    return sum(resultados_possiveis)