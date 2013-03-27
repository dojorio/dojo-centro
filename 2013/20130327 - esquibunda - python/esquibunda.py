#-*- coding: utf-8 -*-

def esquibunda(montanha):
	if montanha:
		max_index = montanha[0].index(max(montanha[0]))
		return len(montanha[0][:max_index + 1])

	return len(montanha)
