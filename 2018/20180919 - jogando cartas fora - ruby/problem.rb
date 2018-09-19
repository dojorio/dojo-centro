def cartasfora(cartas)
	if(cartas == 3 )
		return [[1, 3], 2]
  elsif( cartas == 5)
  	return [[1, 3, 5, 4], 2]
  elsif(cartas == 7)
		return [[1, 3, 5, 7, 4, 2], 6]

	elsif(cartas == 4)
		return [[1, 3, 2], 4]

	elsif(cartas == 6)
		return [[1, 3, 5, 2, 6], 4]
	
	end
end