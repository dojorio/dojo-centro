def problem(ord)
	output = [[]]
	value = 1
	for i in 0..ord-1
		output[i][i] = value
	end
    return output
end