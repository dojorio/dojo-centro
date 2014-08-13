def bigger_jump(distance, stones)
  return distance if stones.empty?
  return 1 if stones.count == 2

  if stones[0][0] == 'B'
    return distance - stones[0][1..-1].to_i
  end

  distance
end
