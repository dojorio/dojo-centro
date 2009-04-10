def pegarPrimeiroDigito(entrada):
    linhas = entrada.split('\n')
    digito = []
    for linha in linhas:
        digito.append(linha[:3])
    return '\n'.join(digito)

def pegarSegundoDigito(entrada):
    linhas = entrada.split('\n')
    digito = []
    for linha in linhas:
        digito.append(linha[3:])
    return '\n'.join(digito)
    
def conversor(entrada):
    if entrada == """\
   
  |
  |""": return 1
    if entrada == """\
 _ 
 _|
|_ """:   return 2
    if entrada== """\
 _ 
 _|
 _|""":   return 3
    if entrada == """\
   
|_|
  |""":   return 4
    if entrada== """\
 _ 
|_ 
 _|""":     
        return 5
    elif len(entrada) > 11:
        primeiro_digito = pegarPrimeiroDigito(entrada)
        segundo_digito = pegarSegundoDigito(entrada)
        primeiro_digito, segundo_digito = conversor(primeiro_digito), conversor(segundo_digito)
        return int(str(primeiro_digito) + str(segundo_digito))