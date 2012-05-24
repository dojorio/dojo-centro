def americusto(consumo):
    tabela = ((1000000, 7), (10000, 5), (100, 3), (0, 2))
 
    for limite, taxa in tabela:
        if consumo > limite:
            return americusto(limite) + (consumo - limite) * taxa

    return 0
    
def conta(soma, distancia):
    if(soma <= 200):
        return (soma - distancia) / 2
    else:
        for i in range(distancia):
            if americusto(i) == distancia:
                break
        for j in range(soma):
            if americusto(a) + americusto(b) == soma
                break

