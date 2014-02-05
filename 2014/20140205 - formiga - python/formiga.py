import math

def onde_está(tempo):
	quadrado = math.sqrt(tempo)
	if str(quadrado).isdigit():
		if tempo % 2 == 0:
			y = 0
			x = quadrado
		else:
			x = 0
			y = quadrado
	else:

	    if tempo >= 9:
	        return (tempo-9, 3)
	    elif tempo >= 6:
	        return (8-tempo, 2)
	    x = tempo // 2     
	    y = (tempo + 1) //2 % 2 
	    return (x  , y)