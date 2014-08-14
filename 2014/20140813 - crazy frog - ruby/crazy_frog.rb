
def bigger_jump(distance, stones)

  return distance if stones.empty?

  betweens = stones.map do | stone |
    stone[1..-1].to_i
  end

  stones
    
  if stones.count == 2
    to_end = distance - stones[1][1..-1].to_i
    between = stones[1][1..-1].to_i - stones[0][1..-1].to_i
    from_start = stones[0][1..-1].to_i

    return [from_start,between,to_end].max
  end

  if stones[0][0] == 'B'
    return distance - stones[0][1..-1].to_i
  end

  distance
end
