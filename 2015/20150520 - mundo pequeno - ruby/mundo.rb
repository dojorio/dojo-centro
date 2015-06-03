def povo_perto(amigos, visitado)
  origem = amigos.delete(visitado)

  binding.pry

  distancias = amigos.map do |nome, posicao|
    [nome, distancia(origem, posicao)]
  end.sort_by { |amigo| amigo[1] }

  binding.pry

  distancias = distancias.first(3)

  distancias.map(&:first)
end

def distancia(a, b)
  dx = (a[0] - b[0]) ** 2
  dy = (a[1] - b[1]) ** 2

  (dx + dy) ** 0.5
end