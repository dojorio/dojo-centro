def smider_pan(buildings)  
  saltos = 2
  status = ?s
  atual = buildings.shift

  buildings.each_with_index do |proximo, i|
    if proximo > atual && status == ?s
      saltos += 1

      atual = proximo
    end

    if proximo < atual
      if buildings.size > i+1 && buildings[(i+1)..-1].min > proximo
        next
      end

      status = ?d
      saltos += 1

      atual = proximo
    end
  end

  return saltos
end