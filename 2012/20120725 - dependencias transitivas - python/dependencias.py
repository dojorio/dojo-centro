# coding: utf-8

def dependencias(entrada):
    saida = dict(entrada)

    for item, lista in entrada.items():
        for dependencia in lista:
            for elemento in entrada.get(dependencia, []):
                if elemento not in lista and elemento != item:    
                    lista.append(elemento)
        lista.sort()
                    
    return saida
