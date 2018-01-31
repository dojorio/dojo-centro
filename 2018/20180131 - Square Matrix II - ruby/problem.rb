def problem(ord)
	output = [[]]
	value = 1

	for i in 0..ord-1
		output[i][i] = value
	end

	for i in 0..ord-1
		# preenche apos 1
		for j in i..ord-1
			output[i][j+1] = j + 1 
		end
		for j in ord-1..0
			output[i][j-1] = j - 1
		end
	end

    return output
end