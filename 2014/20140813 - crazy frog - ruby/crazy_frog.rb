def bigger_jump(distance, stones)
  return distance if stones.empty?
  if stones.count == 2
    return 1 
  end

  if stones[0][0] == 'B'
    return distance - stones[0][1..-1].to_i
  end

  distance
end
