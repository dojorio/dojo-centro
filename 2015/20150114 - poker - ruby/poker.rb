def maior_carta(mao)
  baralho = [2,3,4,5,6,7,8,9,'T','J','Q','K','A']

  mao.map do |carta|
    baralho.index(carta[0])
  end.max 

end

