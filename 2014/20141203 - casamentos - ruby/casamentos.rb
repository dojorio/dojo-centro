def casamentos(solteiros, solteiras)
  quantidade_solteiros = solteiros.count - solteiras.count
  quantidade_solteiros > 0 ? [quantidade_solteiros, solteiros.min] : [0]
end

def casais(solteiros, solteiras)
  return [] if solteiras.empty?

  lista_casais = []

  solteiros.sort.reverse.each do |solteiro|
    diff = 1000
    index_solteira = 0

    solteiras.each_with_index do |solteira, index|
      local_diff = (solteiro - solteira).abs
      if local_diff < diff
        diff = local_diff
        index_solteira = index

        break if local_diff == 0
      end
    end

    lista_casais << [solteiro, solteiras[index_solteira]]
    solteiras.delete_at(index_solteira)

    break if solteiras.empty?
  end

  lista_casais
end