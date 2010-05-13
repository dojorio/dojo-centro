# -*- coding: utf-8 -*-
def parser(transicoes, estados_finais, expressao):
    
            
    if expressao.endswith('9') and not '++' in expressao and not '99' in expressao:
        return True

    return False    


def executa_transicao(estado_atual,transicao):
    if estado_atual == 0:  
        return 1

    return 0
