def smider_pan(buildings)  
  saltos = 2
  status = ?s
  anterior = buildings.shift

  buildings.each do |building|
    if building > anterior && status == ?s
        saltos += 1
    end

    if building < anterior
      status = ?d
      saltos += 1 
    end
    anterior = building
  end
  return saltos
  if buildings.size == 4
    if buildings[0] < buildings[1]
      return 5
    else
      return 4
    end
  end

  if buildings.size == 3
    if buildings[0] < buildings[1]
      if buildings[1] < buildings[2]
        return 4
      else
        return 3
      end
    elsif buildings[0] > buildings[1]
      if buildings[1] > buildings[2]
        return 4
      else
        return 3
      end
    elsif buildings[1] < buildings[2]
      return 3
    else
      return 2
    end
  end

  if buildings.size == 2 && buildings[0] != buildings[1]
    return 3
  end

  2
end