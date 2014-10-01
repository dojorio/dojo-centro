def ballroom(height, width, planks)
  area = width * height

  if planks.include? area
    1
  elsif planks.reduce(:+) != area
    "impossivel"
  else
    planks.size
  end
end