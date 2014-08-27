def bigger_jump(distance, stones)
  return distance if stones.empty?

  positions = stones.map do |stone|
    if stone[0] == 'B'
      stone[1..-1].to_i 
    end
  end.compact

  positions.push(distance)

  last = 0

  betweens = positions.map do |position|
    between = position - last
    last = position
    between
  end

  return betweens.max
end
