require 'prime'

def estrela_da_val(pontos)
  # if Prime.prime?(pontos)
  #   return pontos / 2
  # end

  # case pontos
  # when 8, 10, 12
  #   2
  # when 9
  #   3
  # else
  #   1
  # end

  if pontos < 5
    return 1
  elsif pontos.even?
    return 2
  elsif pontos == 3
    return 6
  else
    (pontos / (pontos-1) / 2) + 1
  end
end