def prize(value, bet, drawed)
  verifier = bet % 100 - 1
  drawed = drawed % 100
  drawed = 99 if drawed == 0

  return value * 16 if verifier / 4 == drawed / 4
  
  0
end