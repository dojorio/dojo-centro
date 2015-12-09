def prize(value, bet, drawed)
  bet    = bet % 10
  drawed = drawed % 10

  bet    = 10 if bet == 0
  drawed = 10 if drawed == 0

  return value * 50 if bet == drawed
  return value * 16 if (bet - 1) / 4 == (drawed - 1) / 4
  
  0
end