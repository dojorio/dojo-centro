
class Espiral(object):
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas

        self.matriz = {}

        valor = 1

        for coluna in range(0, colunas):
            self.matriz[(0, coluna)] = valor
            valor += 1

        for linha in range(1, linhas):
            self.matriz[(linha, colunas-1)] = valor
            valor += 1

        for coluna in range(colunas-2, 0, -1):
            self.matriz[(linhas-1, coluna)] = valor
            valor += 1

        for linha in range(linhas-2, 0, -1):
            self.matriz[(linha, 0)] = valor
            valor += 1


    def linha(self, i):
        resultado = []

        for coluna in range(self.colunas):
            resultado.append(self.matriz[(i, coluna)])

        return resultado

    def coluna(self, i):
        resultado = []

        for linha in range(self.linhas):
            resultado.append(self.matriz[(linha, i)])

        return resultado

