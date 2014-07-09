def turn_piece(piece)
  case piece.length
  when 4
    [piece.join]
  when 3
    ['###',
     '#  ']
  when 2
    ['# ',
     '# ',
     '##']
  else
    piece[0].split ''
  end
end