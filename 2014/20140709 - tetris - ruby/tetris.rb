def turn_piece(piece)
  if piece.length == 4
    [piece.join]
  else
    piece[0].split ''
  end
end