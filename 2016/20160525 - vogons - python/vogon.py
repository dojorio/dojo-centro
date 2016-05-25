def vogon_report(road_start, road_end, planets):
	if planets[0][1] == 0 and road_start[0] == 0 and road_end[0] >= planets[0][0]:
		return {"deaths": planets[0][2]} 
	else:
		return {"deaths": 0}
