def bigger_jump(distance, stones)
  return distance if stones.empty?

  positions = stones.map do |stone|
    stone[1..-1].to_i
  end

  positions.push(distance)

  last = 0

  betweens = positions.map do |position|
    between = position - last
    last = position
    between
  end

  return betweens.max

  # if stones[0][0] == 'B'
  #   return distance - positions[0]
  # end

  # distance
end
