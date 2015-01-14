def maior_carta(mao)
  baralho = '  23456789TJQKA'

  mao.map do |carta|
    baralho.index(carta[0])
  end.max

end

