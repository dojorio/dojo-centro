def routes_number(edges, origin, destination, max_distance)
  distance = edges.first[2].to_i
  
  if edges.first[0] != origin 
    return 0
  end


  if distance <= max_distance
    return 1
  end

  return 0
end