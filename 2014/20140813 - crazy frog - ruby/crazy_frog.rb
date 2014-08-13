def bigger_jump(distance, stones)
  if !stones.empty?
    return distance - stones[0][1].to_i
  end
  
  distance
end