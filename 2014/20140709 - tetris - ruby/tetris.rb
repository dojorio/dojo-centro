def turn_piece(piece)
  lines = piece.length
  output = piece[0].split('')

  (1...lines).each do |i|
    output = output.zip(piece[i].split('')).reverse
  end

  output.map(&:join)
end