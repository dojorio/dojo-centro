def ballroom(height, width, planks)
  if planks.include? (width * height)
    return 1
  end

  if planks.first < width
    return "impossivel"
  end
  planks.size
end