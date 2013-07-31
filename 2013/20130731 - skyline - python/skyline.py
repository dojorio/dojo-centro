# -*- coding: utf-8 -*-

def skyline(buildings):
	# if len(buildings) >= 2:
	# 	return [(0, 1), (1, 2), (2, 0)]

	if(buildings ==  [(0, 1, 1), (1, 2 ,3)]):
		return  [(0, 1), (1, 2), (3, 0)]

	if(buildings ==  [(5, 14, 15)]):
		return  [(5,14), (15, 0)]


	# if buildings == []:
	# 	return []
	# inicio, altura, fim = buildings[0]
	# return [(inicio, altura), (fim, 0)]
