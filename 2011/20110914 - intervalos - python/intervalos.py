def eh_consecutivo(primeiro, segundo):
    return (primeiro + 1) == segundo

def intervalos(numeros):
    intervalos = [[numeros[0]]]
    
    for i in range(len(numeros)-1):
        if not eh_consecutivo(numeros[i], numeros[(i+1)]):
            intervalos[-1].append(numeros[i])
            intervalos.append([numeros[i+1]])

    return map(tuple, intervalos)
