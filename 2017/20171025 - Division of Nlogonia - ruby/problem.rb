def division_of_nlogonia division, points
	if points.size == 1
	  if points[0][0] > division[0] && points[0][1] > division[1]
	    return ['NE']
	  end

	  if points[0][0] < division[0] && points[0][1] > division[1]
	  	return ['SE']
	  end

	  if points[0][0] < division[0] && points[0][1] < division[1] 
	  	return ['SO']
	  end

		if points[0][0] < division[0] && points[0][1] > division[1] 
	  	return ['NO']
	  end

	  return ['divisa']
	else
		result = []
		points.each do|point|
			result += division_of_nlogonia(division, [point])
	end
		return result
	end
end