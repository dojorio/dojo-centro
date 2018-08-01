def max_sum(cards, player_quantity)
  cards_values = {'A' => 1, '2' => 2}
  cards = cards.map do | card |
    cards_values[card]
    end
  cards.length
end