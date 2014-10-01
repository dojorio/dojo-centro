def ballroom(height, width, planks)
  area = width * height
  sum = 0

  count = 0

  planks.sort.reverse.each_with_index do |plank, index|
    return 1 if plank == area
    
    if sum + plank <= area 
      sum += plank 
      count += 1
    end

    return count if sum == area
  
  end

  "impossivel"
end