def prize(value, bet, drawed)
  value * case
  when bet % 10000 == drawed % 10000
    3000
  when bet % 1000 == drawed % 1000
    500
  when (bet %= 100) == (drawed %= 100)
    50
  when ((bet) +3) / 4 == ((drawed) +3) / 4
    16
  else
    0
  end
end
