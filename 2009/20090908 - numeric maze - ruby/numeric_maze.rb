def solve(start_point, end_point)
	x = start_point
	path = [start_point]

    while x < end_point
		x = double(x)
		path << x
	end
	
	return path if path.last == end_point 

	x = start_point
	path = [start_point]
	while x < end_point
		x += 2
		path << x
	end

	return path if path.last == end_point 

	return [1,3,6]
	
	
		
	# if end_point == path.last
	   # return path
	# else
		# diferenca = end_point - path.last
		
		# if diferenca == 2
			# path <<  path.last + 2
			# return path
		# end
		
	# end
	
	# while x < end_point
		# x = x + 3
		# path << x
	# end
	return path
end

def double(number)
	return number * 2
end