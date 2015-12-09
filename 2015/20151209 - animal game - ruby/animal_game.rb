def prize(value, bet, drawed)
  verifier = bet - 1200
  drawed = 100 if drawed == 0

  return value * 16 if verifier / 4 == drawed / 4

  
  0
end