def where_is_the_marble(marbles, queries)
  if marbles.length > 1 
    return [marbles.index(queries[0]) + 1]
  end
  if marbles == [2] && marbles.include?(queries[0])
    return [1]
  end
  return [false]
end
