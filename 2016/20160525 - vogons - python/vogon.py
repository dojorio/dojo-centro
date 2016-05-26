def vogon_report(road_start, road_end, planets):
	road_start_x = road_start[0] 
	road_start_y = road_start[1]
	road_end_x = road_end[0]
	road_end_y = road_end[1]

	planet = planets[0]

	if road_start_x <= planet[0] <= road_end_x:
		if road_start_y <= planet[1] <= road_end_y:
			return {"deaths": planet[2]}
		elif  road_start_y >= planet[1] >= road_end_y:
			return {"deaths": planet[2]}
	elif road_start_x >= planet[0] >= road_end_x:
		if road_start_y <= planet[1] <= road_end_y:
			return {"deaths": planet[2]}
		elif  road_start_y >= planet[1] >= road_end_y:
			return {"deaths": planet[2]}
	return {"deaths": 0}
