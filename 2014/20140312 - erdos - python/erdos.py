def classificaErdos(pessoa, livros):
    conjunto = ['Erdos']

    dic_counter = 0;

    while livros:
        if pessoa in conjunto:
            return dic_counter

        dic_counter += 1

        for autor in conjunto:
            for livro in [livro for livro in livros if autor in livro]:
                if pessoa in livro:
                    return dic_counter
                else:
                    for autor_livro in [autor_livro for autor_livro in livro if autor_livro not in conjunto]:
                        conjunto.append(autor_livro)
                livros.remove(livro)
