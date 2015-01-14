def maior_carta(mao)

  maior_carta 
  mao.each do |carta|
    numero_da_carta = carta[0].to_i

    if numero_da_carta == 0
      #T J Q K A
      # if carta[0] == 'Q'
      #   return carta
      # end

      # if carta[0] == 'J'
      #   return carta
      # end
    end
  end

  mao.max
end

