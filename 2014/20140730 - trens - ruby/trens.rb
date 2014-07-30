def routes_number(edges, origin, destination, max_distance)
  first_path = edges[0]
  distance = first_path[2].to_i
  
  if first_path.first != origin 
    return 0
  end


  if distance <= max_distance
    return 1
  end

  return 0
end