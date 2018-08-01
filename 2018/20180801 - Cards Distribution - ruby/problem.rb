def max_sum(cards, player_quantity)
  cards_values = Hash.new { |hash, key| key.to_i }.merge({
    'A' => 1,
    'J' => 11,
    'Q' => 12,
    'K' => 13
  })

  cards.map { |card| cards_values[card] }.reduce(&:+) / player_quantity
end