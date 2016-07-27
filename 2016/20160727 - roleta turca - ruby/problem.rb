def max_profit(roulette, balls)
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