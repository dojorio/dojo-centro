def turn_piece(piece)
  if piece.length == 1
    piece.split('')
  else
    [piece.join('')]
  end
end