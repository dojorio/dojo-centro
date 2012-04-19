def beverage_sort(beverages, relations):
    lista = list(beverages)
    lista.sort(lambda x, y: -1 if (x, y) in relations else 1)
    return tuple(lista)

