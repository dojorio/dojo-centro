def where_is_the_marble(marbles, queries)
  result = []

  if queries.length > 1
    if marbles.include?(queries[0])
      result.push(marbles.index(queries[0]) + 1) 
      if marbles.include? (queries[1])
        result.push(marbles.index(queries[1]) + 1)
      else
        result.push(false) 
      end
    else
      result.push(false)
      if marbles.include? (queries[1])
        result.push(marbles.index(queries[1]) + 1)
      else
        result.push(false) 
      end
    end
  else
    if marbles.length > 1 
      result.push(marbles.index(queries[0]) + 1)
    else
      if marbles.include?(queries[0])
        result.push(marbles.index(queries[0]) + 1)
      else
        result.push(false)
      end
    end
  end
  return result
end
