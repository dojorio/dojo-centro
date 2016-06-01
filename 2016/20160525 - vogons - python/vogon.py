def vogon_report(start, end, planets):
	start_x, start_y = start
	end_x, end_y = end

	planet = planets[0]

	if (start_x <= planet[0] <= end_x or
		start_x >= planet[0] >= end_x):
		if (start_y <= planet[1] <= end_y or
			start_y >= planet[1] >= end_y):
			return {"deaths": planet[2]}

	return {"deaths": 0}
