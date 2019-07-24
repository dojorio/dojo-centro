def smider_pan(buildings)  
  saltos = 2
  status = ?s
  atual = buildings.shift

  buildings.each_with_index do |proximo, i|
    if proximo > atual
      if status == ?s
        saltos += 1
      end
      if status == ?d
        status = ?s
      end
    end
    if proximo < atual
      saltos += 1
      status = ?d
    end

    atual = proximo
  end

  return saltos
end