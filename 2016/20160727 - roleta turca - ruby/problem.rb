def max_profit(roulette, balls)
	
  if roulette.count(1) >= 2  
  	return balls[0] * -2 
  end
  if roulette.count(-1) >= 2
  	return balls[0] * 2
  end

  return balls[0] * -1

  
   
  0
end