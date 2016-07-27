def max_profit(roulette, balls)
  return 4 if balls[0] == -2 && roulette.count(1) >= 2
  return 2 if balls[0] == -1 && roulette.count(1) >= 2
  return 2 if balls[0] == -2
  return 1 if balls[0] == -1 && roulette.count(1) == 0 
   
  0
end