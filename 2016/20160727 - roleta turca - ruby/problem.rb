def max_profit(roulette, balls)
  ball = balls[0]
  roulette_sum = roulette.reduce(:+)

  if roulette.size==3
    if ball > 0 
       sum_2_min = roulette_sum - roulette.max
       return sum_2_min * -ball
    else
      sum_2_max = roulette.reduce(:+) - roulette.min
      return sum_2_max * -ball
    end  
  end
  0
end