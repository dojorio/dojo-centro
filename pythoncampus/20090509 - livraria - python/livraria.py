def calcular_preco(lista_de_livros):
    quantidade_de_livros = sum(lista_de_livros)
    lista_de_livros = filter (None, lista_de_livros)
    contador = len(lista_de_livros)
    taxas = {1 : 1, 2 : 0.95}
    return 42*quantidade_de_livros * taxas[contador]

