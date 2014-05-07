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
    for padrão in padrões:
      if padrão != último_padrão:
        resultado = aplica_padrao(linha, padrão)
        resultados_possiveis.append(resultado)
      último_padrão = padrão


  return max(resultados_possiveis)