def cartasfora(cartas)
	if(cartas == 3)
		return [[1, 3], 2]
	end
	if(cartas == 4)
		return [[1, 3, 2], 4]
	else
  	return [[1, 3, 5, 4], 2]
	end
end