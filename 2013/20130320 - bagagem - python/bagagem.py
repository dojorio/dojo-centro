#-*- coding: utf-8 -*-
def divisivel(malas):
	if len(malas) == 2 and malas[0] == malas[1]:
		return True
	if len(malas) == 3:
		return True

	return not malas
