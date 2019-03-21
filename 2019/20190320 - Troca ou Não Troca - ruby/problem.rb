def troca_ou_nao(rodadas)
  maior  = rodadas.size + 1
  trocas = 0
  
  while rodadas[0][0] != maior
    rodadas.shift
  end

  rodada = rodadas[0]

  if rodada[1] == 0
    trocas += 1
  end

  rodadas.shift

  rodadas.each do |rodada|
    trocas += rodada[1]
  end

  trocas
end