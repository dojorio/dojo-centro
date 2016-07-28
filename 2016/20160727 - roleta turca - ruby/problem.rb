def max_profit(roulette, balls)
  ball = balls[0]

  max = -(roulette.reduce(:+) * ball).abs

  roulette.each_with_index do |e, i|
    next_e = roulette[(i + 1) % roulette.size]

    if (e + next_e) * -ball > max
      max = (e + next_e) * -ball
    end    
  end

  max
end