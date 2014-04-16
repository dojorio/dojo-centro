def coelho(ovos, velocidade)
  velocidade_atual = velocidade / 2
  qnt_de_ovos = 0

  if ovos.size == 2
    ovos.each do |ovo|
      velocidade_atual = (ovo[1] / velocidade_atual)
      return 1 if velocidade_atual < 720
      qnt_de_ovos = qnt_de_ovos + 1 
    end
    return qnt_de_ovos
  end
  y = ovos[0][1]
  if y / velocidade_atual < 720
    1
  else
    0
  end
end