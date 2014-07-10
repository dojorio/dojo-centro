def turn_piece(piece)
  lines = piece.length
  output = piece[lines - 1].split('')

  return output if lines == 1

  (lines - 2).downto(0) do |i|
    output = output.zip(piece[i].split(''))
  end

  output.map(&:join)
end

def min_filled_spaces(board, piece)
  blocks = board.reduce(0){ |memo, row| memo + row.count('#')}

  if blocks == 6
    piece.length == 1 ? 0 : 10
  else
    (blocks + 4) % 10
  end
end
