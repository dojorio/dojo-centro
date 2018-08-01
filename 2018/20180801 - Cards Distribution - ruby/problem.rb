def max_sum(cards, player_quantity)
  cards_values = Hash.new { |hash, key| key.to_i }.merge({
    'A' => 1,
    'J' => 11,
    'Q' => 12,
    'K' => 13
  })

  cards = cards.map { |card| cards_values[card] }
  groups = cards.each_slice(cards.length / player_quantity).to_a

  groups.map { |group| group.reduce(&:+) }.max
end