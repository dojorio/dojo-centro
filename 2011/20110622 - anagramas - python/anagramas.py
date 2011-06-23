#'abc'
#'a  bc', 'a  cb', 'b  ac', 'b  ca', 'c  ab', 'c  ba'
#'abcd', 'acbd', 'b  ac', 'b  ca', 'c  ab', 'c  ba'

def anagramas(palavra):
    resultado = set()
    
    if not palavra:
        resultado.add(palavra)
    else:
        for letra in palavra:
            palavra_sem_letra = palavra.replace(letra, "", 1)
            for anagrama in anagramas(palavra_sem_letra):
                resultado.add(letra + anagrama)
                
       
    return resultado
