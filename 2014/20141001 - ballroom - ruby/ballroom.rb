def ballroom(height, width, planks)
  area = width * height
  sum = 0

  planks.sort.reverse.each_with_index do |plank, index|
    return 1 if plank == area

    sum += plank if sum + plank <= area
    return index + 1 if sum == area
  end

  "impossivel"
end