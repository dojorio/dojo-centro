def ballroom(height, width, planks)
  area = width * height

  sum = 0
  planks.each do |plank|
    sum += plank
    if sum == area
      return planks.index(plank) + 1
    end
  end

  if planks.include? area
    1  
  elsif planks.reduce(:+) != area
    "impossivel"
  else
    planks.size
  end
end