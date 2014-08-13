
def bigger_jump(distance, stones)

  return distance if stones.empty?

  if stones.count == 2
    to_end = distance - stones[1][1..-1].to_i
    from_start = stones[0][1..-1].to_i

    if to_end > from_start
      return to_end
    else
      return stones[0][1..-1].to_i
    end
  end

  if stones[0][0] == 'B'
    return distance - stones[0][1..-1].to_i
  end

  distance
end
