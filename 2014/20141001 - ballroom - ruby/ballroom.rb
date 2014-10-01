def ballroom(height, width, planks)
  if planks.include? (width * height)
    return 1
  end
  planks.size
end