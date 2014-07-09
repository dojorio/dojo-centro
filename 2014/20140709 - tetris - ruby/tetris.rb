def turn_piece(piece)
  case piece.length
  when 4
    [piece.join]
  when 3
    ['###',
     '#  ']
  when 2
    piece[1].split('').zip(piece[0].split('')).map(&:join)

  else
    piece[1].split('').zip(piece[0].split('')).map(&:join)
  end
end