def ballroom(height, width, planks)
  area = width * height
  sum = 0

  count = 0

  planks.sort.reverse.each do |plank|
    return 1 if plank == area

    if sum + plank <= area
      sum += plank
      count += 1
      return count if sum == area
    end
  end

  "impossivel"
end