require 'prime'

def estrela_da_val(pontos)
  estrelas_validas = 1

  (2..(pontos/2)).each do |step|
    visitados = []
    ponto_atual = 1

    (1..pontos).each do
      visitados << ponto_atual

      if visitados.uniq.length == pontos
        estrelas_validas += 1
      end

      ponto_atual += step
      ponto_atual = ponto_atual % pontos if ponto_atual > pontos
    end
  end

  return estrelas_validas
end