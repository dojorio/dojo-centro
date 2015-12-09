def prize(value, bet, drawed)
  value * case
  when bet % 10000 == drawed % 10000
    3000
  when bet % 1000 == drawed % 1000
    500
  when (bet %= 100) == (drawed %= 100)
    50
  else
    bet    = 100 if bet == 0
    drawed = 100 if drawed == 0

    (bet - 1) / 4 == (drawed - 1) / 4 ? 16 : 0
  end
end
