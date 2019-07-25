def smider_pan(buildings)  
  status = ?s
  atual = buildings.shift

  buildings.reduce(2) do |saltos, proximo|
    diff = 0

    if proximo > atual
      if status == ?s
        diff = 1
      else
        status = ?s
      end
    end

    if proximo < atual
      diff = 1
      status = ?d
    end

    atual = proximo

    saltos + diff
  end
end