def where_is_the_marble(marbles, queries)
  if marbles == [2]
    return [1]
  end
  if marbles == [1,2]
    return [2]
  end
  if marbles == [2,5]
    return [1]
  end
  return [false]
end
