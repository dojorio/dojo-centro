def max_sum(cards, player_quantity)
  cards_values = Hash.new { |hash, key| key.to_i }.merge({
    'A' => 1,
    'J' => 11,
    'Q' => 12
  })

  cards.map { |card| cards_values[card] }.reduce(&:+)
end