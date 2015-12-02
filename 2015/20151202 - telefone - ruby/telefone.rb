def telefone_de(nome)
  case nome
  when 'D', 'E', 'F'
    '3'
  when 'G', 'H', 'I'
    '4'
  when 'J', 'K', 'L'
    '5'
  when 'M', 'N', 'O'
    '6'
  else
    '2'
  end
end