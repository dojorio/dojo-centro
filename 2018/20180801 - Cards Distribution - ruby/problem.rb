def max_sum(cards, player_quantity)
  cards_values = Hash.new { |hash, key| key.to_i }.merge({
    'A' => 1,
    'J' => 11,
    'Q' => 12,
    'K' => 13
  })

  cards = cards.map { |card| cards_values[card] }
  groups = cards.each_slice(cards.length.fdiv(player_quantity).ceil).to_a

  first = groups.map { |group| group.reduce(&:+) }.max
  return first if groups.length == 1 || groups[0].length == 1

  groups[1].unshift(groups[0].pop)
  second = groups.map { |group| group.reduce(&:+) }.max

  [first, second].min
end