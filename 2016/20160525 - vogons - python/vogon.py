def vogon_report(road_start, road_end, planets):
	road_start_x = road_start[0] 
	road_start_y = road_start[1]
	road_end_x = road_end[0]
	road_end_y = road_end[1]

	if planets[0][1] == 1:
		return {"deaths": 0}
	if planets[0][0] >= road_start_x and 
		planets[0][0] <= road_end_x:	
		return {"deaths": planets[0][2]} 
	else:
		return {"deaths": 0}
