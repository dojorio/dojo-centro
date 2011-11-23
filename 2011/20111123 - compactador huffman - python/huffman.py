
def valor(no):
    return no[1]
    
def esquerda(no):
    return no[2]

def direita(no):
    return no[3]
    
def eh_terminal(no):
    return valor(no)

def percorrer(no, tabela, prefixo):
    if eh_terminal(no):
        tabela[valor(no)] = prefixo
    else:
        percorrer(esquerda(no), tabela, prefixo + '0')
        percorrer(direita(no), tabela, prefixo + '1')
    
def tabela_compactacao(arvore):
    if arvore == ():
        return {}
    
    eh_terminal = valor(arvore)
    if eh_terminal:
        return { valor(arvore): '0' }
    
    tabela = {}
    percorrer(arvore, tabela, '')
    return tabela
    
class CaractereNaoIndiciadoError:
    pass
    
def compactar(tabela, cadeia):     
    try:
        return ''.join(map(tabela.get, cadeia))
    except TypeError:
        raise CaractereNaoIndiciadoError
""" roubado vvv
def visitar(arvore, no, cadeia):
    if eh_terminal(no): 
        return valor(no) + visitar(arvore, arvore, cadeia)
    if cadeia == '': return ''
    elif cadeia[0] == '0':
        return visitar(arvore, esquerda(no), cadeia[1:])
    else:
        return visitar(arvore, direita(no), cadeia[1:])
        
def descompactar(arvore, cadeia):
    return visitar(arvore, arvore, cadeia)
"""