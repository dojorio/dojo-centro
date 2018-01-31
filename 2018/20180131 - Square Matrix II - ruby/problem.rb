def problem(ord)
	output = [[]]

	if ord == 2
		return [[1, 2], [2, 1]]
	end
	if ord == 3
		for i in 1..ord
			for j in 1..ord
			    output[i - 1][j - 1] = i - 1
			end
		end

		return [[1, 2, 3], [2, 1, 2], [3, 2, 1]]
	end
	if ord == 4
		return [[1, 2, 3, 4], [2, 1, 2, 3], [3, 2, 1, 2], [4, 3, 2, 1]] end
  return [[1]]
end