def jogo(*jogadas)
  if jogadas.include? 'tesoura' and jogadas.include? 'papel'
    :tesoura

  elsif jogadas.include? 'papel' and jogadas.include? 'pedra'
    :papel

  elsif jogadas.include? 'pedra' and jogadas.include? 'tesoura'
    :pedra

elsif jogadas.first == jogadas.last
    :empate



  end
end

