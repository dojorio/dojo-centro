#-*- coding: utf-8 -*-

def tentar(malas, soma):
	if soma == 0: return True
	if len(malas) == 0 or soma < 0: return False
	return tentar(malas[0:-1], soma-malas[-1]) or tentar(malas[0:-1], soma)

def divisivel(malas):
	if sum(malas) % 2:
		return False

	return tentar(malas, sum(malas)/2)
