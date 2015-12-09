def prize(value, bet, drawed)
  bet    = bet % 100
  drawed = drawed % 100

  bet    = 100 if bet == 0
  drawed = 100 if drawed == 0

  return value * 50 if bet == drawed
  return value * 16 if (bet - 1) / 4 == (drawed - 1) / 4
  
  0
end