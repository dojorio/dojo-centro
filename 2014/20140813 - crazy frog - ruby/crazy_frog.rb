def bigger_jump(distance, stones)
  
  if !stones.empty?
    if stones[0] == 'B'
      return distance - stones[0][1..-1].to_i
    end
  end
  
  distance
end