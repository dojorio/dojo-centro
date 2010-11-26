from random import randint


class AmigoOculto:
    def sortear(self, amigos):
        
        
        pulo = randint(1,2)
        
        sorteados = amigos[pulo:] + amigos[:pulo]
        
        
        
        
        return sorteados

