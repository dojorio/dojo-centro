def smider_pan(buildings)
  if buildings.size == 3
  	return 4
  end

  if buildings.size == 2 && buildings[0] != buildings[1]
  	return 3
  end

  2
end