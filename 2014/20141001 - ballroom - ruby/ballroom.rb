def ballroom(height, width, planks)
  area = width * height

  sum = 0
  planks.each_with_index do |plank, index|
    return 1 if plank == area
    sum += plank
    if sum == area
      return index + 1
    end
  end

  "impossivel"
end