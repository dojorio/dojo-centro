def ballroom(height, width, planks)
  if planks.include? (width * height)
    1
  elsif planks.reduce(:+) < (width * height)
    "impossivel"
  else
    planks.size
  end
end