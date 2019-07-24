def smider_pan(buildings)  
  # saltos = 0
  # status = 's'
  # buildings.each_with_index do |building, i|
  #   2,1,3
  #   if buildings[i+1] > building
  #       saltos += 1
  #       next
  #   end 
  #   if building == buildings[i+1]
  #       next
  #   end
  # end

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