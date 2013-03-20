#-*- coding: utf-8 -*-

def tentar(malas, soma):
	if len(malas) == 0:
		return True


	return tentar(malas[:-1], soma-malas[-1]) or tentar(malas[:-1], soma)

def divisivel(malas):
	if sum(malas) % 2:
		return False

	if len(malas) == 1:
		return False

	if len(malas) == 2 and malas[0] == malas[1]:
		return True

	if len(malas) == 3 and (
		malas[1] + malas[2] == malas[0] or
		malas[0] + malas[1] == malas[2] or
		malas[0] + malas[2] == malas[1]):
		return True

	if len(malas) == 4 and (
		malas[0] + malas[1] + malas[2] == malas[3] or
		malas[0] + malas[1] == malas[2] + malas[3]):
		return sum(malas) % 2 == 0

	return not malas
