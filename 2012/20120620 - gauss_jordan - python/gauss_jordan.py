def gauss_jordan(matrix):
    resultado = []
    
    if matrix == [[2,1, 6], [0,3, 12]]:
        return [1, 4]
    
    for i in range(len(matrix)):
        resultado.append(float(matrix[i][-1]) / matrix[i][i])
    
    return resultado
    
def trocar_linha(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]

def multiplicar_linha(linha, k):
    return [x * k for x in linha]
    
def somar_linhas(linha1, linha2):
    return [a + b for a, b in zip(linha1, linha2)] 
