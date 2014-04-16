def coelho(ovos, velocidade)
  velocidade_atual = velocidade / 2

  y = ovos[0][1]
  if y / velocidade_atual < 720
    1
  else
    0
  end
end