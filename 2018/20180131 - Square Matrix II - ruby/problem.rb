def problem(ord)
	output = [[]]
	value = 1

	for i in 0..ord-1
		output[i][i] = value
	end

	for i in 0..ord-1
		# preenche apos 1
		for j in i..ord-1
			output[i][j] = i+1 
		end

		# preenche antes do 1
		for 
			
		end
	end

    return output
end