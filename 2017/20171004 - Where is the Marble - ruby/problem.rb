def where_is_the_marble(marbles, queries)
  if queries.length > 1
    if marbles.include?(queries[0]) 
      return [1,false]
    end
    return [false,false]
  end
  if marbles.length > 1 
    return [marbles.index(queries[0]) + 1]
  end
  if marbles.include?(queries[0])
    return [1]
  end
  return [false]
end
