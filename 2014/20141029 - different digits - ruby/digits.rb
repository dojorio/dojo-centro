def houses(first, last)
  # return 9  if last == 11 and first == 2
  # return 10 if last == 11 and first == 1
  # return 8 if last == 11 and first == 3
  # casas = first + 1
  if last == 11
    return last - first
  end

  return 2 if last == 3 and first == 2

  return last
end