def max_profit(roulette, balls)
  ball = balls[0]
  roulette_sum = roulette.reduce(:+)

  if ball > 0
     sum_2_min = roulette_sum - roulette.max
     return sum_2_min * -ball
  end

  sum_2_max = roulette.reduce(:+) - roulette.min

  if ball > 0
  return sum_2_max * (-ball)
end
  if roulette.count(1) >= 2
    return balls[0] * -2 
  end

  if roulette.count(-1) >= 2
    return balls[0] * 2
  end

  if balls[0] > 0 &&
    roulette.all? { |n| n >= 0 } && roulette.count(0) >= 2 
    return 0
  end

  if roulette.count(2) >= 2
    return (roulette[1] + roulette[2]) * -2
  end

  balls[0] * -1
end