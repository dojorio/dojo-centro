def routes_number(edges, origin, destination, max_distance)
  graph = edges.reduce({}) do |memo, edge|
    memo.merge(edge[0] => { edge[1] => edge[2..-1].to_i })
  end

  if edges.first[0] != origin && edges.last[0] != origin 
    return 0
  end

  if edges.first[1] != destination && edges.last[1] != destination 
    return 0
  end

  if first_distance <= max_distance || last_distance <= max_distance
    return 1
  end

  0
end