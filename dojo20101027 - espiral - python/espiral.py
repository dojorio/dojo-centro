def foo(colunas, espacador, linhas=1):
    numeros = range(linhas, colunas + linhas)
    tamanho = len(str(colunas))
    return espacador.join([str(numero).rjust(tamanho) for numero in numeros])


def espiral(linhas, colunas):
    if linhas == colunas == 2:
        return foo(colunas, ' ', 1) + '\n' + foo(colunas, ' ', 3)[::-1]

    if linhas > 1:
        return foo(linhas, '\n')
    else:
        return foo(colunas, ' ')

