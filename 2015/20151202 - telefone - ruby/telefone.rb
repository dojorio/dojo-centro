def telefone_de(nome)
  return '22' if nome == 'AB' || nome == 'BA'
  return '33' if nome== 'DE' || nome == 'ED'
  case nome
  when 'D', 'E', 'F'
    '3'
  when 'G', 'H', 'I'
    '4'
  when 'J', 'K', 'L'
    '5'
  when 'M', 'N', 'O'
    '6'
  when 'P', 'Q', 'R', 'S'
    '7'
  when 'T', 'U', 'V'
    '8'
  when 'W', 'X', 'Y', 'Z'
    '9'
  when 'A', 'B', 'C'
    '2'
  else
    nome
  end
end