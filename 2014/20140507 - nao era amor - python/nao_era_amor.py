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
    resultados_da_linha = []

    for padrão in padrões:
      if padrão != último_padrão:
        resultado = aplica_padrao(linha, padrão)
        resultados_da_linha.append(resultado)

    melhor_da_linha = max(resultados_da_linha)
    resultados_possiveis.append(
      padrões[resultados_da_linha.index(melhor_da_linha)])


  return max(resultados_possiveis)