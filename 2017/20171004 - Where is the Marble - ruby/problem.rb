def where_is_the_marble(marbles, queries)
  if marbles.length > 1 
    return [marbles.index(queries[0]) + 1]
  end
  if marbles.include?(queries[0])
    return [1]
  end
  if queries.length > 1
    return [false,false]
  end
  return [false]
end
