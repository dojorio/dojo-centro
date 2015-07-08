def efeito_magnetico(magnetos, raio, ponteiro)
  distancia = 1_000_000_000
  magneto_pos = ponteiro
  raio_2 = raio ** 2

  magnetos.each do |magneto| 
    distancia_2 = (magneto.first - ponteiro.first) ** 2 +
                  (magneto.last - ponteiro.last) ** 2

    if distancia_2 < raio_2 && distancia_2 < distancia
      magneto_pos = magneto
      distancia = distancia_2
    end
  end
  
  magneto_pos
end