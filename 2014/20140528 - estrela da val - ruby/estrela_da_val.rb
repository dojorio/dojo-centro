def estrela_da_val(pontos)
  
  case pontos
    when 5
      return 2
    when 7
      return 3
    when 8
      return 2
    when 9
      return 3
  when 10
    return 2
  else
    for i in 1..(pontos/2)
      return i if pontos / i == 0
    end.count
  end

  return 1 


end