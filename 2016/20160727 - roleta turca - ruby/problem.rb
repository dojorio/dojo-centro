def max_profit(roulette, balls)
  ball = balls[0]
  roulette_sum = roulette.reduce(:+)

  if roulette.size == 3
    if ball > 0
       sum_2_min = roulette_sum - roulette.max
       return sum_2_min * -ball
    else
      sum_2_max = roulette.reduce(:+) - roulette.min
      return sum_2_max * -ball
    end
  end

  min = roulette_sum * ball

  roulette.each_with_index do |e, i|
    next_e = roulette[(i + 1) % roulette.size]

    if (e + next_e) * ball < min 
      min = (e + next_e) * ball
    end    
  end
  return min

  # 0
end