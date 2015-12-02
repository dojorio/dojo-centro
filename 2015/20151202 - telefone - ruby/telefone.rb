def telefone_de(nome)
  nome.split('').map do |letra|
    case letra
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
      letra
    end
  end.join
end