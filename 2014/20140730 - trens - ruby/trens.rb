def routes_number(edges, origin, destination, max_distance)
  first_distance = edges.first[2].to_i
  last_distance = edges.last[2].to_i

  if edges.first[0] != origin && edges.last[0] != origin 
    return 0
  end

  if first_distance <= max_distance || last_distance <= max_distance
    return 1
  end

  0
end