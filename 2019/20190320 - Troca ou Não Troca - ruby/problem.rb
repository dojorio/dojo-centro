def troca_ou_nao(rodadas)
  maior = rodadas.size + 1

  if rodadas[0][1] == 0
    return 1
  end

  if rodadas.size > 1 && (rodadas[1][1] == 1 && rodadas[1][0] != maior) 
    return 1
  end

  0
end