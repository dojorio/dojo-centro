def routes_number(edges, origin, destination, max_distance)
  first_path = edges[0]
  distance = first_path[2].to_i
  if distance <= max_distance
    return 1
  end

  return 0
end