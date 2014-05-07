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

  for padrão in padrões:
    for linha in tabuleiro:
      resultado = aplica_padrao(linha, padrão)
      resultados_possiveis.append(resultado)

  return max(resultados_possiveis)